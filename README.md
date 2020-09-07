# CookBook

If you are learning to cook, trying new cuisines or may be you have taken your first step as an adult and moved separate in a new house, this website will not only provide you with the recipes but will also mention the tools you need and a link to buy them.
You may be vegan or non-vegetarian, fear not as this website provides all the types of recipes. 
Have a particular cuisine you gravitate towards, dont worry, this website takes into consideration 40 different cuisines 
This website pretty much does all the research for you, all you need to do is decide what you fancy eating today.

Amateur or professional cook, this website not only lets you view other recipes but also allows you to contribute and share you amazing recipes.

## UX

This website is for anyone that wants to learn to cook, try out new recipes or share their own recipes.

Below are some user stories :
1. __User wants to add a recipe but does not have an account and username entered already exists:__  
    User clicks on the new recipe tab on the navbar, user has not logged in, he will be directed to the login page.
    User then clicks on the signup link at the bottom. The sigup form appears, user types in a username that 
    already exists, a message is displayed informing the user that the username already exists and the signup 
    page is displayed again. User fills the form with different values, a message is displayed informing the 
    user was successful in creating the account and taken to the home page. User then clicks on the new recipe tab and 
    fills the form clicks on submit.
      
2. __User wants to add a recipe but does not have an account and chooses a unique username:__  
    user clicks on the new recipe tab from the navbar, user has not logged in, he will be directed to the login page.
    User then clicks on the signup link at the bottom. The sigup form appears. user fills the form, 
    a message is displayed informing the user was successful in creating the account and taken to the home 
    page. User then clicks on the new recipe tab and 
    fills the form clicks on submit. 
      
3. __User wants to add a recipe and has signed up already but logs in with wrong details:__  
    User clicks on the new recipe tab, user has not logged in, he will be directed to the login page.
    User fills the form, clicks on login button, error message is displayed informing that the
    login details were not matching. User fills the form with correct values, a message is displayed welcoming 
    the user and taken to the home page. User then clicks on the new recipe tab, fills the form and clicks on submit button.
    
4. __User wants to add a recipe and has signed up already and logs in with correct details:__  
    User clicks on the new recipe tab. user has not logged in, he will be directed to the login page.
    User fills the form, clicks on login button, message is displayed welcoming the user and taken to the home 
    page. User then clicks on the new recipe tab and fills the form clicks on submit.

5. __User wants to add a recipe and is already logged in and fills the form with invalid values:__  
    User clicks on the new recipe tab, fills the form and clicks on submit. Error message appears. users 
    changes the value as requested and clicks on submit again. Form gets saved in the database and the user
    is redirected to the homepage

5. __User wants to add a recipe and is already logged in and fills the form with valid values:__  
    User clicks on the new recipe tab. fills the form clicks on submit. Form gets saved in the database and the user
    is redirected to the homepage
    
6. __User wants to view the recipe but no recipe available:__  
    The user clicks on search on the nav bar or explore button on the homepage, chooses the cuisine, clicks on submit. The user is alerted saying that there are no recipes 
    available yet for that cuisine. The user then changes the cuisine value, click on submit, click on the arrow
    next to the recipe title that he wants to view

7. __User wants to view the recipe and recipe available:__  
    The user clicks on search, chooses the cuisine, clicks on submit, click on the arrow next to the recipe 
    title that he wants to view

8. __User wants to edit the recipe and has not logged in:__ 
    User views the recipe, scrolls down, clicks on edit button, message displayed asking the user to log in and redirected to the login page
    
8. __User wants to edit the recipe created by some other user:__  
    User has already logged in, views the recipe, scrolls down, clicks on edit button, error message is displayed "Cannot edit recipes
    created by other users" and redirected to the search page

9. __User wants to edit his own recipe but enters invalid values:__  
    User has already logged in, views the recipe, scrolls down, clicks on edit button, gets redirected to the form which are filled dynamically
    with the existing values, user then edits the fields as required, clicks on update button, error message is displayed "invalid format".
    User then changes the values of the fields as required, clicks on update again, values in the database
    get updated and user is redirected to the view page of that particular recipe

10. __User wants to edit his own recipe but enters valid values:__  
    User views the recipe, scrolls down, clicks on edit button, gets redirected to the form which are filled dynamically
    with the existing values, user then edits the fields as required, clicks on update button, values in the database
    get updated and user is redirected to the view page of that particular recipe

11. __User wants to delete the recipe created by some other user:__  
    User views the recipe, scrolls down, clicks on delete button, error message displayed "Cannot delete recipes
    created by other users" and redirected to the search page.

12. __User wants to delete his own recipe:__  
    User views the recipe, scrolls down, clicks on delete button, a pop up message is displayed asking the user
    *"Are you sure you want to delete this whole recipe? Yes/No"*. If the user clicks on no, pop up message disappears.
    If user clicks on yes, recipe gets deleted and user is transfered to the homepage.
    
13. __User wants to buy the tools listed with the recipe:__  
    User is currently on the view page of a recipe, scrolls down at the tool section, clicks on the name of the tool needed,
    new tab gets opened with the link to buy it.

14. __User wants to view the full list of tools recommended:__  
    Users clicks on buy tab from the navbar, gets a list of all the tools listed on the website, clicks on the arrow
    next to the name of the tool, new tab gets opened with the link to buy it.

15. __User views the dashboard:__  
    User clicks on the dashboard tab from the navbar, views the statistics and charts.

16. __User wants to log out:__  
    User is already logged in, the log out option becomes visible on the navbar, user clicks on it, users is logged out and taken
    to the homepage

__During the early stages, a rough__ [wireframe](static/pdf/Cookbook_wireframe.pdf) __was made using balsamiq__  


## Features

### Existing Features:
Navigation: allows the user to choose between what they want to acheive by clicking on the tab (code in: base.html).

Add recipes: allows users to add a recipe by filling out the add recipe form (code in: new_recipe.html)

search: allows users to choose which recipe they want to view, edit and/or delete by choosing the cuisine from a drop down

view a recipe: allows the users to view the entire recipe by clicking on the name of the recipe

edit recipe: allows the users to update values in a recipe by clicking on the edit button and making changes to the form values

delete: allows the users delete the recipes no longer needed by clicking on the delete button

buy a tool: allows the users the view the recommended tools and buy them by clicking on the name of the tool

dashboard: allows the users to view some charts

login/signup: allows the users to login to an account/create an account to manipulate values saved in the database by filling out the username and password

### Features Left to Implement
* Allow to download, share and rate the recipes
* Provide an option to mark the recipes as favourites
* Create a detailed login in form, so that if a user forgets his password there's an option to reset it
* Have a profile page which would list the users contribution to the website along with his personal data
* In the add new recipe and edit form allow to delete a field
* By default, in the search page have the user's country as the selected country 


## Technologies Used

**HTML:** Hypertext Markup Language (HTML) was used to create the webpage. 

**CSS:** Cascading Style Sheets (CSS) was used to add customised styling to the webpage.

**JavaScript:**  JavaScript enables interactive web pages and is an essential part of web applications. It was used to add interactive functionality to the webpage

**Python:** Python was used for the server side web development. Also to connect to the database and perform various operations of its data.

**Flask:** [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a micro web framework written in python. Flask provides tools and libraries to build a webpage or application. 

**Mongodb:** [Mongodb](https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=bing&utm_campaign=bs_emea_united_kingdom_search_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=386028215&msclkid=ceee6c15f9b31def4751334385c068b9) was 
the database used to store the data for this web application. 
It is a document database, which means it stores data in JSON-like documents.

**Mongodb Charts:** [Mongodb-Charts](https://www.mongodb.com/products/charts) was used to create the charts displayed on the dashboard. 
Mongodb charts helps to create visualisation of the mongodb data. 
There are two ways of embedding a chart in this project the charts have been embedded using sdk, so that when the data has been manipulated by the user, it is reflected in the charts.

**Materialize:** [Materialize](http://archives.materializecss.com/0.100.2/)  was used to the reduce the frontend production time, as it comes with pre designed classes which can be added to any project

**Balsamiq:** [Balsamiq](https://balsamiq.com/) was used to create wireframe. It was used in the initial stages of the project visualisation. It was used to put the idea of a page decide the layout and flow of the project. 

**JQuery:** [JQuery](https://jquery.com/) was used to simplify DOM manipulation.

## Testing

Manual testing was done on all the forms of this project

**New recipe form:**  
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with an invalid url format and verify that a relevant error message appears.  
Try to submit the form with an invalid title and verify that an error message about the invalid format appears.  
Try to submit the form with an invalid calories and verify that an error message about the invalid format appears.  
Try to submit the form with all inputs valid and verify that the values get stored in the database.  

**Edit recipe:**  
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with an invalid url format and verify that a relevant error message appears.  
Try to submit the form with an invalid title and verify that an error message about the invalid format appears.  
Try to submit the form with an invalid calories and verify that an error message about the invalid format appears.  
Try to submit the form with all inputs valid and verify that the fields get updated correctly.  

**Delete recipe**
Try to delete a recipe entered by another user and verify that an error message appears.  
Try to delete a recipe entered by the same user and verify that a warning message appears.  
Try to choose the *No* option and verify that the recipe is not deleted from the database.  
Try to choose the *Yes* option and verify that the recipe is deleted from the database.  

**Login page**
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with an details not matching and verify that a relevant error message appears.  
Try to submit the form with all inputs valid and verify that the success message appears.   

**Signup page**
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with an existing username value and verify that a relevant error message appears.  
Try to submit the form with all inputs valid and verify that the success message appears.  

## Deployment

This project is used using [Heroku](https://dashboard.heroku.com/apps).  
Steps taken to deploy this project are as follows:  
* Create an app in Heroku  
* In the terminal typed the follow commands:  
    1. heroku login  
    1. heroku apps
    1. git init
    1. pip3 freeze --local > requirements
    1. echo web: python <span>app.py</span> > Procfile
    1. git add.
    1. git commit -m "initial commit"
    1. heroku git ::remote
    1. git push heroku master
    1. heroku ps:scale web=1
* In the herko app, go to settings:
    1. IP = 0.0.0.0
    1. PORT = 5000
 
* All the environment values have been saved in the env.py file

## Credits


### Content
The recipes have been copied from:  
* [The Spruce Eats](https://www.thespruceeats.com/)  
* [Cook With Manali](https://www.cookwithmanali.com/)  

Links for tools have been copied from:  
* [Amazon](https://www.amazon.co.uk/)

### Media
The recipe images are taken from:
* [The Spruce Eats](https://www.thespruceeats.com/)
* [Cook With Manali](https://www.cookwithmanali.com/)

The backdrop image is taken from:
* [Redcurry](https://d1wcgy4dy6voh7.cloudfront.net/wp-content/uploads/2016/03/redcurry.jpg)

## Acknowledgements

I received inspiration for this project from:  
* [The Spruce Eats](https://www.thespruceeats.com/)
* [Cook With Manali](https://www.cookwithmanali.com/)

Many of the development problems have been rectifies with the guidance of 
* [StackOverflow](https://stackoverflow.com/)
* [code Institue tutors](https://courses.codeinstitute.net/login)