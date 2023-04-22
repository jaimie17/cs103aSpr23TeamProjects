/*
  transaction.js -- Router for the Transactions
*/
const express = require('express');
const mongoose = require( 'mongoose' );
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
    const sortBy = req.query.sortBy;

    let items = []
    if (id) { // if ID is present, delete the corresponding transaction and show all the remaining ones
      await Transaction.deleteOne({ _id: id, userId: req.user._id }); // delete the transaction from the database
      items = await Transaction.find({ userId: req.user._id }); // fetch all the remaining transactions
    } else if (sortBy == 'category') {
      items = await Transaction.find({ userId: req.user._id }).sort({ category: 1 });
    } else if (sortBy == 'amount') {
      items = await Transaction.find({ userId: req.user._id }).sort({ amount: 1 });
    } else if (sortBy == 'description') {
      items = await Transaction.find({ userId: req.user._id }).sort({ description: 1 });
    } else if (sortBy == 'date') {
      items = await Transaction.find({ userId: req.user._id }).sort({ date: 1 });
    } else {
      items = await Transaction.find({ userId: req.user._id })
    }

    res.render('transaction', { items });
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

router.get('/transaction/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/edit/:itemId")
      const item = 
       await Transaction.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('edit_transaction')
      //res.json(item)
});

router.post('/transaction/update/',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId} = req.body;
      console.log("inside /transaction/edit/:itemId");
      const item = {
        description:req.body.description,
        category:req.body.category,
        amount:req.body.amount,
        date:req.body.date
      };
      
      await Transaction.findOneAndUpdate({_id: itemId}, item);
      res.redirect('/transaction')
});

router.get('/transaction/groupByCategory',
  isLoggedIn,
  async (req, res, next) => {
      const userId = req.user._id;
      let categories =
            await Transaction.aggregate(
                [ 
                  { 
                    $match: {
                      userId: new mongoose.Types.ObjectId(userId)
                   }
                 },
                   { 
                     $group: {
                      _id: '$category',
                      total: { $sum:'$amount' }
                    }
                  }         
                ]);
  
        res.render('groupByCategory', {categories})
});

module.exports = router;
