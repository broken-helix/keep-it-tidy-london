# **Litter Pickers London**
## **Site Overview**

Litter Pickers London is a site dedicated to spreading the word about Litter Picking and creating a community via user-organised litter picking events.

[View the live project here](https://pickers-london-f5f0f470e555.herokuapp.com).

![Responsive Screenshot](/docs/am-i-responsive.jpg)
***

## Table of contents:
1. [**Site Overview**](#site-overview)

2. [**Planning stage**](#planning-stage)
    * [***Site Aims***](#site-aims)
    * [***Database Plan***](#database-plan)
    * [***Wireframes***](#wireframes)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Color Scheme***](#color-scheme)
    * [***Typography***](#typography)
3. [**Current Features**](#current-features)
    * [***Home Page***](#home-page)
    * [***Navigation***](#navigation)
    * [***Events Page***](#events-page)
    * [***Event Details Page***](#event-details)
    * [***Add Event Page***](#add-event)
    * [***Edit Event Page***](#add-event)
    * [***Delete Event Page***](#add-event)
    * [***Add Comment***](#add-comment)
    * [***Attend Event***](#attend-event)
    * [***Alerts***](#alerts)
    * [***User Accounts***](#user-accounts)
4. [**Future-Enhancements**](#future-enhancements)
5. [**Testing Phase**](#testing-phase)
6. [**Deployment**](#deployment)
7. [**Tech**](#tech)
8. [**Credits**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**General reference**](#general-reference)
    * [**Content**](#content)
***

## **Planning stage**

### **Site Aims:**

* To introduce the user to litter picking
* To host litter picking events
* To build a community via attending icons and comments
* To build an interactive site using DJANGO with CRUD functionality
***

### **Database Plan:**

![Database Plan](/docs/images/drawsql.jpg)
***

### **Wireframes:**

Wireframes were used to plan out the design of the site on desktop and mobile devices.

![Desktop Wireframe](/docs/images/mobile-home-wireframe.png)

![Mobile Wireframe](/docs/rockpaperscissorsmobilewireframe.jpg)
***

### **Target Audiences:**

* People who want to find out more about Litter Picking.
* People who want to organise litter picking events in London.
* People who want to find organised litter picking events in London.
***

### **User Stories:**

An Agile Approach was followed in the planning and construction of the site.  User stories were built using GitHub Issues, grouped into Epics for different aspects of the site design (structure, administration, content creation etc...), attached to a Milestone and organised onto a board.  Each user story has a list of tasks to tick off and an acceptance criteria.  As stories were built, they were moved to the Not Started column of the board.  Once they were started, they were moved to the In Progress Column and finally, when all tasks were complete, the story was moved to the complete column and marked closed.  Each story was listed in relevant Epic as a task and ticked off when the story was complete.

The project board can be viewed here: [Litter Pickers London Project Board](https://github.com/users/broken-helix/projects/7/views/1).

*Stories*

* **SITE ADMINISTRATION:** As a **manager of the site** I can **login to the admin panel** so that **I can manage the site**.
* **ADMIN PANEL CUSTOMISATION:** As a **site administrator** I can **use the admin panel to filter and search content and use a WYSIWYG editor and auto-generate slugs** so that **I can easily add and manage content**.
* **ADD IMAGES TO EVENTS IN ADMIN PANEL:** As an **admin** I can **add images in the admin panel** so that **I can add images to events**.
* **VIEW A HOME PAGE:** As a **user** I can **view a home page** so that **I can understand what the site is about**.
* **VIEW AN EVENTS PAGE:** As a **user** I can **view an events page** so that **I can see a list of events**.
* **VIEW EVENT DETAILS:** As a **user** I can **click a link on the events page** so that **I can see the details of the individual event on a new page**.
* **SITE PAGINATION:** As a **user** I can **see a paginated list of events** so that **I can view a few posts at a time**.
* **VIEW ATTENDEE NUMBER:** As a **user** I can **see the total number of attendees for an event** so that **I can see how many people are attending**.
* **USER ACCOUNT CREATION:** As a **user** I can **create an account** so that **I can use the account to add content**.
* **ADD COMMENTS TO EVENT:** As a **user** I can **add comments to an event when logged in** so that **I can add comments to an event**.
* **ATTEND EVENTS:** As a **user** I can **mark that I am attending an event** so that **I can show my interest in an event**.
* **MESSAGES:** As a **user** I can **see messages to let me know my action has been carried out** so that **I receive information about my actions**.
* **ADD EVENT:** As a **registered user** I can **add an event** so that **I can list my event on the site**.
* **EDIT EVENT:** As a **registered user** I can **edit my own event** so that **I can correct mistakes and update details**.
* **DELETE EVENT:** As a **registered user** I can **delete my events** so that **remove my events from the site**.
* **AUTO COMPLETE SLUG AND ORGANISER FIELDS:** As a **registered user** I can **auto complete slugs and organiser fields** so that **they are created automatically**.
* **RESTRICT PERMISSIONS:** As an **event organiser** I can **prevent others from editing or deleting my events** so that **my events are not edited or deleted by other users**.



*Epics*

* 
***

### **Color Scheme:**

The color scheme was designed to incorporate natural greens, browns and yellows, to reflect the environmental aspect, along with complementary colors.
Colors were selected using the coolors color palette generator.  <br><br>

![Coolors Palette](/docs/images/litter-pickers-ldn-palette.png)
***

## **Typography**

* The fonts used throughout the site were selected from Google Fonts.
* Fonts were selected for their simple and readable design to avoid distracting from the content.
* Inter, Kanit and Open Sans were selected


![Font selection](/docs/url.jpg)
***

## **Current Features**

#### *Home Page:*

* The page title clearly indicates to the user what the site is about, in the choice of words and positioning at the top of the page, outside of the game area. A seperate colour was used to separate it from the game itself.

![Page Title](/docs/title.jpg)

#### *Events Page:*

* The events page displays a list of events to the user.  In desktop views, the events are organised into rows of three, with six events per page.

![Game Area](/docs/desktop-view.jpg)

#### *Events Details Page:*

* The events details page display the event in more detail
* Each event has a unique url including both the slug and id of the event.

#### *Add Event Page:*

* The events details page display the event in more detail.  A comment form is displayed to logged in users.  Comments must be approved in the admin panel.  An attending button is clickable if the user is logged in.

#### *Edit Event Page:*

* The edit event page is linked with an edit link which is only displayable to the logged in user who created the event.

#### *Delete Event Page:*

* The delete event page is linked with an delete link which is only displayable to the logged in user who created the event.

#### *Add Comment:*

* A logged in user can create and submit a comment which is displayed to the user only, until approved. A total of approved comments is located on the page.

#### *Attend Event:*

* Logged in users can click the total number of attendees icon to indicate their interest in attending the event.  When done, the icon changes to idicate that the user had pressed the button.

#### *Alerts:*

* Bootstrap alerst are displayed to the user when certain actions are carried out, such as adding a comment, adding a post, creating an account or logging in or out.

#### *User Accounts:*

* User accounts can be created via the 'Register' link in the navbar and require just a username, email and password.

## **Future-Enhancements**

* Allow the user to search for events in their borough
* Allow the user to create a personal profile page
* Allow users to add reports of litter picks
* Allow users to add images to comments
* Allow users to use a page to request litter picks in their street or area.
* Links to other information.
***

## **Testing Phase**

* Responsiveness - A mobile-first approach was used to develop the site, using the iPhone 12 profile in Chrome dev tools.  The site was tested for responsiveness on different screen sizes throughout the development stages, using chrome dev tools, which allowed the page to be adjusted to display on small and large screen sizes with media queries.  The site was also tested using firefox on a desktop, on an android mobile phone using chrome, on an ipad and iphone 6 using safari and designed to display correctly.
​
* Functionality - The nature of Django means that many errors are picked up before deployment, as they frequently make themselves obvious while testing is set to True, with pages not loading or redirecting properly.  At each stage of development, the functionality has been tested to maske sure it works and these tests have been included in the list of task inside the User Stories on GitHub.

* Contrast - The contrast on the page was checked using the WCAG Color contrast checker plugin in chrome and found to pass the tests, after adjustments to the colours and background and restricting colour changes to the inner parts of the elements and not the borders.

![WCAG Color Contrast Results](/docs/url.jpg)

* Lighthouse - The site was checked using the Lighthouse chrome plugin and found to pass the tests.

![Lighthouse Desktop Results](/docs/lighthouse-desktop.jpg)

![lighthouse Mobile Results](/docs/lighthouse-mobile.jpg)
​
* Validators - The W3C validator was used to check both HTML and CSS, with the only error found that the validator didn't validate the google scripts code at the top of the CSS file.  JShint was utilised to check the javscript and some minor errors were found which do not affect the functionality of the site.

![HTML Validator](/docs/html-validation.jpg)

![CSS Validator](/docs/css-validation.jpg)

![CSS Validator Error](/docs/css-validation-error.jpg)

![JS Validator Error](/docs/jshint-result.jpg)
***

## **Bugs**


***

## **Deployment**

I deployed the page on Heroku pages via the following procedure:
​
1. 
​
The live site can be found at the following URL - [Litter Pickers London](https://pickers-london-f5f0f470e555.herokuapp.com/).
***

## **Tech**
​
The following technologies were employed in the creation of the site:
​
- HTML
- CSS
- JS
- Bootstrap
- Django
- Balsamiq Wireframes
***

## **Credits**

### **Honorable mentions**

* Once again, I would like to thank my mentor, Richard Wells, who gave me some great insights into models and kept me motivated.
***

### **Content:**

* Fonts were sourced from [Google Fonts](https://fonts.google.com/).

* Icons were sourced from [Font Awesome](https://fontawesome.com/icons).

* Wireframes were created using the [Balsamiq Wireframes](https://balsamiq.com/wireframes/) application.