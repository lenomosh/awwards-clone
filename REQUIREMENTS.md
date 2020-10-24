# 2. Overall Description
## 2.1 Project prompt

At Moringa school you create a lot of projects (IPs, Mid-week projects) but you never know how those projects rate with your peers. Your objective is to create an application like Awwards (Links to an external site.) (It doesn't necessarily have to be exactly the same). The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

A project can be rated based on 3 different criteria

1. Design
2. Usability
3. Content

These criteria can be reviewed on a scale of 1-10 and the average score is taken.
## 2.2 User stories

As a user, I would like to:

    1. View posted projects and their details
    2. Post a project to be rated/reviewed
    3. Rate/ review other users' projects
    4. Search for projects 
    5. View projects overall score
    6. View my profile page

## 2.3 User environment

Your application should be accessible to users on both desktop and mobile formats. You must ensure that your application is responsive to different screen sizes.
## 2.4 UI Design requirements

Your application should have a clean, simple, well-organized user interface. Ensure you choose a consistent color scheme and use appropriate fonts for your application. Also, you MUST create a mockup design for your application before you begin development.

You can use the following resources to design your application:

    1. Pen and Paper - For Mockup design.
    2. Bootstrap (Links to an external site.) - For simple responsive UI elements
    3. Coolors (Links to an external site.) - For Color scheme generation.
    4. Google fonts (Links to an external site.) - For beautiful fonts

# 3. System Features/Objectives
## Feature A: Projects

Projects should have a Title, an image of the project's landing page, a detailed description of the project, a link to the live site.
## Feature B: Profile

Your project should have a user profile that at least the following information:

    Profile picture of the user
    User Bio
    Projects the user has posted
    A contact information of the user

## Feature C: An Authentication System 

Your application should have a solid authentication system that allows users to sign up or log in to the application before posting or rating a project.
## Feature D: Rating/ Review

Projects will be rated/reviewed based on the following criteria:

    Design - This is the overall appearance of the project
    Usability - This can be translated to the user experience and how responsive the project is.
    Content - This includes the technologies used, the font used(is it uniform throughout the project) and grammar

These criteria will each be rated/review on a scale of 1-10 and the overall score will be their average.
## Feature E: API Endpoints

You should create an API so that users can access data from your application. You can create two API endpoints:

    Profile - This endpoint should return all the user profiles with information such as the username, bio, projects of the user and profile picture
    Projects- This endpoint should return information pertaining to all the projects posted in your application.

# 4. Other Nonfunctional Requirements
## 4.1 Software quality attributes

Your code should be written following the Python pep 8 guidelines (Links to an external site.). Make sure you document major sections of your code using docstrings. Also, ensure you commit regularly and your commit messages are clear and well written.
## 4.2 Project Tests

Your project should have tests to test the core behaviours. All your tests should pass. 
4.3 Project documentation

You should have a well-documented README for your project. You can follow this template README (Links to an external site.) to write your README file.

 
## 4.4: Deployment

Your project should be deployed to Heroku when you have finished with the set features. You should provide the link to your project in the description part of your project repository.