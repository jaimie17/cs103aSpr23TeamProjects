## PA04: Transaction App in Express/Mongoose

We are recreating PA03 app as an Express App using Mongodb (through Mongoose) as the database. This app has an home, about, to do list, transaction and a logout page. 

### Teammates:
 1. Samiya
 2. Jaimie
 3. Cindy
 4. Gianna


## Task/Description of Transaction page features:

#### Five buttons: 
1. group by category
2. sort by category
3. sort by amount
4. sort by description
5. sort by dates

#### Sort by
Clicking on the sort by category button, adds a query parameter   ?sortBy=category
and returns to the same page except the category column. Similarly with the other three sort by buttons that mostly sorts alphabetically.

#### Group By Category
Hitting the "group by category" link sends you to a page with a simple table with two columns: one for the category and the other for the sum of the amounts for transactions in that category.

