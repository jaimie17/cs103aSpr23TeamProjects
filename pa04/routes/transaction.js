/*
  transaction.js -- Router for the Transactions
*/
const express = require('express');
const router = express.Router();
const Transaction = require('../models/Transaction')
const User = require('../models/User')


/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// get the value associated to the key
router.get('/transaction/',
  isLoggedIn,
  async (req, res, next) => {
      const id = req.query.id;
      // const description = req.query.description
      // const category = req.query.category
      // const amount = req.query.amount
      // const date = req.query.date
      let items=[]
      if (id) { // if ID is present, delete the corresponding transaction and show all the remaining ones
        await Transaction.deleteOne({_id: id, userId: req.user._id}); // delete the transaction from the database
        items = await Transaction.find({userId:req.user._id}); // fetch all the remaining transactions
      } else {
         items = 
           await Transaction.find({userId:req.user._id})
      //                   .sort({createdAt:1})

      }
             res.render('transaction',{items});
});


/* add the value in the body to the list associated to the key */
router.post('/transaction',
  isLoggedIn,
  async (req, res, next) => {
      const transaction = new Transaction(
        {description:req.body.description,
         category:req.body.category,
         amount: req.body.amount,
         date: req.body.date,
         userId: req.user._id
        })
      await transaction.save();
      res.redirect('/transaction')
});


router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/remove/:itemId")
      await Transaction.deleteOne({_id: req.params.itemId, _id:req.params.itemId});
      res.redirect('/transaction')
});

router.get('/todo/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /todo/edit/:itemId")
      const item = 
       await ToDoItem.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('edit')
      //res.json(item)
});

router.post('/todo/updateTodoItem',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,item,priority} = req.body;
      console.log("inside /todo/complete/:itemId");
      await ToDoItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {item,priority}} );
      res.redirect('/toDo')
});

router.get('/todo/byUser',
  isLoggedIn,
  async (req, res, next) => {
      let results =
            await ToDoItem.aggregate(
                [ 
                  {$group:{
                    _id:'$userId',
                    total:{$count:{}}
                    }},
                  {$sort:{total:-1}},              
                ])
              
        results = 
           await User.populate(results,
                   {path:'_id',
                   select:['username','age']})

        //res.json(results)
        res.render('summarizeByUser',{results})
});



module.exports = router;
