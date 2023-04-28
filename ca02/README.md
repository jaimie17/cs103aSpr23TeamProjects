## PA04: Transaction App in Express/Mongoose

We are recreating PA03 app as an Express App using Mongodb (through Mongoose) as the database. This app has an home, about, to do list, transaction and a logout page. 

<img width="1359" alt="Screen Shot 2023-04-22 at 6 27 50 PM" src="https://user-images.githubusercontent.com/76130563/233810612-ebd74c45-72c6-4bea-a568-2f24ae793a4d.png">

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

<img width="1338" alt="Screen Shot 2023-04-22 at 6 29 42 PM" src="https://user-images.githubusercontent.com/76130563/233810597-d45d377b-97de-4548-827c-4ed1e5779e92.png">
<img width="1059" alt="Screen Shot 2023-04-22 at 6 31 33 PM" src="https://user-images.githubusercontent.com/76130563/233810604-ac122a00-85e0-4036-a555-68859b4564dc.png">

## CA02: Adding new page called TextTrove: 
We have created TextTrove page that is inside our Productivity App which focused on creating a web application using Express, Mongoose, and EJS frameworks, which utilizes prompt engineering to generate useful responses to specific user queries. 

#### Motivation: 
The theme of the project is "Text Generation and Analysis," from CA01 and the GPT class's methods will be used to generate text in various formats, such as summaries, translations, paraphrases, poems, articles, captions, etc. Additionally, the app will perform text analysis, such as sentiment analysis. The app should include authentication, so users can log in with a username and password, and store information about their API requests in the database. 
