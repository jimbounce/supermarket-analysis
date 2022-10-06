# supermarket-analysis readme.md 

"""
This project was written as part of my (Nigel Cooksley) Python and Machine Learning training on an Institute Of Coding Skills Bootcamp. This Cloud Analytics and Data Science bootcamp was delivered by Edge Hill University, Liverpool, UK from June to September 2022. 

I chose this project from the 3 available projects as I wanted the challenge of some 'messy' raw data of a straightforward commercial situation. The role of a Data Scientist famously involves 80% data wrangling, which is preceived as the 'boring admin' before the real work begins. It is for me though, a large attraction to the profession! 

The problem, the project solved was to predict the busiest day of an apparently fictitious supermarket in Burma in the first quarter of 2020 given only some sales figures from the first quarter of 2019 (but no figures for the reaminder of that year or previous years. 

This project provided me with essential practice in data wrangling and the chance to apply other skills I had developed on the course (which consisted of 20 hours study per week for 4.5 months, weekly assessment deadlines and larger monthly assesssment deadlines). I also learnt (in the good example here) how 'messy' raw data can be and it really made me think about how and which features I should use to provide useful insight. This was just to enable me to eyeball the data. Further feature engineering was required to convert string fields into dummy integer variables for the application of Machine Learning algorithms. 

From feedback from tutors upon my presentation of my insights what makes my project stand out is that I preformed a significant amount of feature engineering as I focussed on decomposing the date field into days of the week and I also introduced further seasonality fields to represent weeks (which I standardised to classify 31 days of January and March into 28 days (4 weeks).

Original Raw Data Features:
Invoice 
ID
Branch
City
Customer type
Gender
Product line
Unit price
Quantity
Tax 5%
Total
Date
Time
Payment
cogs
gross margin percentage
gross income
Rating

In addition to the original features, I created the following fields for exploratory analysis and machine learning requirements:

dow - day of week - a string variable extracted from original date 
Season - which week in Q1 of 2019 - also a string variable extracted from original date 

Dummy variables for ML:

dowsat, dowsun, dowmon, dowtue, dowwed, dowthu, dowfri
aj1, aj2, aj3, aj4, f1, f2, f3, f4, m1, m2, m3, m4


What to Include in your README
1. Project's Title
This is the name of the project. It describes the whole project in one sentence, and helps people understand what the main goal and aim of the project is.

2. Project Description
This is an important component of your project that many new developers often overlook.

Your description is an extremely important aspect of your project. A well-crafted description allows you to show off your work to other developers as well as potential employers.

The quality of a README description often differentiates a good project from a bad project. A good one takes advantage of the opportunity to explain and showcase:

What your application does,
Why you used the technologies you used,
Some of the challenges you faced and features you hope to implement in the future.
ADVERTISEMENT
3. Table of Contents (Optional)
If your README is very long, you might want to add a table of contents to make it easy for users to navigate to different sections easily. It will make it easier for readers to move around the project with ease.

4. How to Install and Run the Project
If you are working on a project that a user needs to install or run locally in a machine like a "POS", you should include the steps required to install your project and also the required dependencies if any.

Provide a step-by-step description of how to get the development environment set and running.

5. How to Use the Project
Provide instructions and examples so users/contributors can use the project. This will make it easy for them in case they encounter a problem – they will always have a place to reference what is expected.

You can also make use of visual aids by including materials like screenshots to show examples of the running project and also the structure and design principles used in your project.

Also if your project will require authentication like passwords or usernames, this is a good section to include the credentials.

ADVERTISEMENT
6. Include Credits
If you worked on the project as a team or an organization, list your collaborators/team members. You should also include links to their GitHub profiles and social media too.

Also, if you followed tutorials or referenced a certain material that might help the user to build that particular project, include links to those here as well.

This is just a way to show your appreciation and also to help others get a first hand copy of the project.

7. Add a License
For most README files, this is usually considered the last part. It lets other developers know what they can and cannot do with your project.

We have different types of licenses depending on the kind of project you are working on. Depending on the one you will choose it will determine the contributions your project gets.

The most common one is the GPL License which allows other to make modification to your code and use it for commercial purposes. If you need help choosing a license, use check out this link: https://choosealicense.com/

Up to this point what we have covered are the minimum requirements for a good README. But you might also want to consider adding the following sections to make it more eye catching and interactive.

Additional README Sections
8. Badges
Badges aren't necessary, but using them is a simple way of letting other developers know that you know what you're doing.

Having this section can also be helpful to help link to important tools and also show some simple stats about your project like the number of forks, contributors, open issues etc...

Below is a screenshot from one of my projects that shows how you can make use of badges:

badges

The good thing about this section is that it automatically updates it self.

Don't know where to get them from? Check out the badges hosted by shields.io. They have a ton of badges to help you get started. You may not understand what they all represent now, but you will in time.

ADVERTISEMENT
9. How to Contribute to the Project
This mostly will be useful if you are developing an open-source project that you will need other developers to contribute to. You will want to add guidelines to let them know how they can contribute to your project.

Also it is important to make sure that the licence you choose for an open-source projects is correct to avoid future conflicts. And adding contribution guidelines will play a big role.

Some of the most common guidelines include the Contributor Covenant and the Contributing guide. Thes docs will give you the help you need when setting rules for your project.

10. Include Tests
Go the extra mile and write tests for your application. Then provide code examples and how to run them.

This will help show that you are certain and confident that your project will work without any challenges, which will give other people confidence in it, too

Extra points
Here are a few extra points to note when you're writing your README:

Keep it up-to-date - It is a good practise to make sure your file is always up-to-date. In case there are changes make sure to update the file where necessary.
Pick a language - We all come from different zones and we all speak different languages. But this does not mean you need to translate your code into vernacular. Writing your README in English will work since English is a globally accepted language. You might want to use a translator tool here if your target audience isn't familiar with English.
ADVERTISEMENT
Wrap Up
There you have it, everything you need to improve your README files, or even get you started with writing your first one.

At this point I am confident that you are in a position to add an interactive and inforamative guide to your next project or even an existing one and make your project standout.

There are many tools which you can also use to automatically generate a README for your project, but it's always a good practice to try it on your own before moving to automation. In case you want to check them out, they include:

Make a README
README Generator
README
If you have read this far I really appreciate it. If you enjoyed this article and found it helpful, please share it so you can help another developer improve their projects.

I would love to see your newly crafted README file. Be sure to share a link with me via any of the links below:

Connect With me at Twitter | YouTube | LinkedIn | GitHub

Do share your valuable opinion, I appreciate your honest feedback!

Enjoy Coding 

"""
