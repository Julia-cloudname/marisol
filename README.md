# **Marisol Furniture Website**

The Marisol Furniture website serves as a portfolio and blog platform designed for potential customers interested in bespoke furniture. This project is developed using the Django framework and incorporates various features that facilitate interaction between customers and furniture specialists. Marisol Furniture offers users the ability to request a consultation call with an expert who can provide insights into custom furniture options, pricing, materials, and more.

[Marisol](https://marisol-801c526b3523.herokuapp.com/) - The live site can be viewed here.

![Am I Responsive?](link)

<hr>

## **TABLE OF CONTENTS**

 - [**User Experience (UX)**](#user-experience)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
    * [The Scope](#the-scope)
 - [**Design**](#design)
    * [Colours](#colours)
    * [Typography](#typography)
    * [Media](#media)
    * [Wireframes](#wireframes)
    * [Database Schema](#database-schema)
 - [**Features**](#features)
   * [Navigation](#navigation)
   * [Footer](#footer)
   * [Home Page](#home-page)
   * [About Page](#about-page)
   * [Build Threads Blog Page](#build-threads-blog-page)
   * [Featured Threads Page](#featured-threads-page)
   * [My Threads Page](#my-threads-page)
   * [Create Build Thread Page](#create-build-thread-page)
   * [Thread Details Page](#thread-details-page)
 - [**Testing**](#testing)
 - [**Technologies Used**](#technology-used)
 - [**Deployment**](#deployment)
 - [**Credits**](#credits)

<hr>

## **USER EXPERIENCE (UX)**

### **User Stories**

Unregistered site user:

- As a user, I can understand the site's purpose as soon as I land on the homepage.
- As a user, I can navigate the site's content without difficulty or confusion.
- As a user, I can view a list of all the blog articles.
- As a user, I can click on and view each blog article so I can view the content.
- As a user, I can view how many likes each blog article has received.
- As a user, I can view approved  comments made on each blog article.
- As a user, I can easily locate and visit social media links.
- As a user, I can sign up and register on the site.

Regsitered site user:

- As a user, I can perform the same actions as an unregistered site user.
- As a user, I can log in and easily make call bookings.
- As a user, I can edit/delete call bookings I have created.
- As a user, I can see my last call booking on the profile page.
- As a user, I can like/unlike blog articles.
- As a user, I can post comments on blog articles.

Site Admin/Superuser:

- As a user, I can perform the same functionalities as unregistered and registered users.
- As a user, I can create, edit and delete blog articles from the admin panel. 
- As a user, I can approve, edit and delete comments to allow control over inappropriate content.
- As a user, I can see a list of booked calls in the admin panel.
- As a user, I can edit and delete booked calls and create new ones if I need this for some reason.

<hr>

### **Agile Methodology**

For planning the development and implementation of the Marisol website, a project kanban board was used as an Agile Tool through Github. This project board utilised issues as 'User Stories', a link can be found [here](https://github.com/users/Julia-cloudname/projects/6).

To help define the functionalities and prioritise key features, these 'User Stories' were broken down into 4 categories of importance; 'Must Have', 'Should Have',  'Could Have' and 'Won't have'.

'Must Have' represents a feature or functionality that is essential to the site, 'Should Have' is a defined requirement needed for the site, 'Could Have' is determined to be optional and 'Won't have' - future functionality that I'm going to do later.

<hr>

### **The Scope**

#### **The Site's Main Goals:**

- Positive User Experience: The primary goal of the Marisol Furniture website is to provide users with an intuitive, efficient, and enjoyable experience. From browsing articles to scheduling consultations, the site aims to create a seamless journey for users.

- Clear Purpose: The site aims to present its purpose and offerings clearly. It allows users to quickly understand that Marisol Furniture is a platform where they can explore custom furniture options, book consultations, and engage with informative content.

- Controlled Functionality: Based on a user's permissions, the website offers controlled functionality. Registered users have access to profile management, consultation booking, and engagement with blog articles, while specialists have the ability to publish articles and manage user interactions.

- User Profile Management: The site emphasizes the importance of user profiles. Users can easily manage their consultation bookings, view details of their reservations, interact with blog posts and engage with other community members.

<hr>

## **DESIGN**

### **Colours**
- For the colour schema of the site I opted for a dark theme for the header and footer, using (colour) with a contrasting lighter neutral page background colour of (colour). 

### **Typography**
- I chose (font) for my Navigation menu and Header Title fonts
- All fonts were sourced through [Google fonts](https://fonts.google.com/).

### **Media**
- [Balsamiq](https://balsamiq.com/) was used for the design of my wireframes.
- Canva was used for the design of the logo
- Drawsql.app was used for the design of the database schema 

### **Wireframes**
Wireframes for each page are linked here:

[Home Page](link)

[Profile](link)

[Booking](link)

[Signup Page](link)

[Login Page](link)

### **Database Schema**
![Database Schema](link)

<hr>

## **FEATURES**

### **Navigation**

#### **Desktop Navigation**

- The navigation menu on the Marisol Furniture Website is designed for easy access to key sections. It offers links to the 'Home', 'Blog', and 'Gallery' pages, providing a clear pathway for users to explore the primary content areas.
- Registered users are provided with additional options in the menu. They'll find a link to their 'Profile Page' for managing their account details. If the user is already logged in, the menu includes a 'Log Out' button, allowing them to securely sign out from their accounts.
- If a user is not logged in, the navigation menu will feature a link to the 'Registration Page', encouraging new users to create accounts or log in to access more features of the site.
- The navigation bar is designed with responsiveness in mind, adapting seamlessly to various screen sizes. On smaller devices, it collapses into a convenient burger menu, ensuring an optimal browsing experience across devices.

![Desktop Nav](docs/read-me/desktop-nav.png)

This feature enhances the user experience by providing easy navigation to essential sections of the Marisol Furniture Website and enabling registered users to manage their accounts efficiently.


#### **Mobile Navigation**

- The mobile version of the Marisol Furniture Website features a convenient burger menu, ensuring a responsive and user-friendly design for smaller screens.
- When users tap on the burger icon, a dropdown menu unfolds, providing easy access to the same essential page links as mentioned before. This includes the primary pages, such as 'Home', 'Blog', and 'Gallery', along with the user-specific dropdown menu.

![Mobile Nav](docs/read-me/desktop-nav.png)

This mobile navigation approach allows users to navigate the site efficiently on their mobile devices, maintaining consistent access to key sections and user account options through the intuitive dropdown menu.

### **Footer**

- Positioned at the bottom of each page, the footer of the Marisol Furniture Website is dedicated to connecting with our audience on various social media platforms.
- While currently featuring placeholders for social media icons, I will add direct links to official profiles across popular networks such as YouTube, Facebook, Twitter, and Instagram in later versions.
![Footer](docs/read-me/footer.png)
