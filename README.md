# Time to Pause Blog

Time to Pause Blog is a blog where people with an interest in mindfulness can come to read blog posts, create an account with the blog to be able to like and comment under blog posts and can also attend mindfulness classes by filling out a form to register their interest in doing so. 

## Project Set Up 

I created Mind Map on Ludic App for ideas of funcitonality of the blog as well as some additional add on features that I would like to include if I have sufficient time at the end of the project to implement. 
![Lucid-Mind-Map](static/images/lucid-map.png)

## Features 

### Navbar
- Fully responsive navbar with links to: Home, About, Blog, Log In and Sign Up.
- This navbar displays on all pages across the blog.
- Navbar adapts if user is signed in or not.
    * Displays a Sign Up and Log In tab if user is not signed in.
    ![Not-Signed-In](static/images/visitor.png)

    * Displays a Log Out Tab if user is signed in. 
    ![Signed-In](static/images/signed-in.png)

## Footer
- Responsive navbar with links to social media websites: Instagram, X and Facebook to encourage visitors to the site to stay in contact with the blog by following it on social media.
- This appears on all pages across the blog. 

## Setting Up Django Workspace

- I used the Django Blog Cheat Sheet from the 'I Think Therefore I Blog' course content in order to set up my workspace for use with Django and supporting libraries. 
- I installed the relevant libraries required which were Django, Gunicorn, Psycopg2, DJ Database URL, Cloudinary and URL Lib 3. 
- I created my app using the command python3 manage.py startapp "timetopause"
- I migrated these changes and then I ran the server to test was my workspace working using the relevant commands.
- I added my app name to the ALLOWED_HOSTS list in the settings.py file.
- Next, I used ElephantSQL to create an extrernal database to support my app. I have an account already with Elephant SQL so I logged into my account. I selected the 'Create New Instance Button' at the top right hand corner of the screen. From here I entered my app name, selected a plan on which I would like this datebase to run and I clicked on the 'Select Region' button at the bottom of the screen. On this page I checked that the region already selected was correct for me and once I had that confirmed I clicked on the 'Review' button at the end of the page. I reviewed the details of my database here and once I was happy with that I selected the button "Create Instance".
- Once I had this database connected I was returned to my dashboard, from here I clicked on the app I had just created which brought me to my app details. I copied the URL name here. 
- I now logged onto my Heorku account and navigated to the dashboard here. I selected the "New" button on the top right hand corner of the screen and selected "Create New App" from the list of options. From here I entered a name for my app and selected the correct region. I selected "Create App" from here.
- Once I had the app created and was returned to the homepage I selected the app I had just created and then clicked on the "Settings" tab from the app homepage. From here I selected to "Reveal Congif Vars". Here I added a Config Var with the Key of DATABASE_URL and the value of the URL name I had copied from the database I had created in Elephant SQL. I selcted "Add" when both fields had been entered.
- Back in my Gitpod workspace for the app I created an env.py file in the top level directory. Here I imported os and added the database url and created a secret key for the project.
- I once again returned to Heorku and clicked into the Settings tab of my project and again revealed config vars and added a new Key of SECRET_KEY and a value of the secret key that I created for the project.
- In Gitpod I opened my settings.py file and using code imported os and dj database url. Here I also changed the code for the SECRET_KEY and set it to get the secret key value from where it was set. I also commented out the old code for the DATABASE value and added in code to point to my new database url that was specified.
- I saved all files and in the termnial I made migrations using the code python3 manage.py migrate.
- I have an account set up with Cloudinary also. This site is used to host images and media from the app to ensure they are always available. I logged into my Cloudinary account and from the dashboard I copied the API Environment Variable. 
- I added this to my env.py file as a separate line of code to point directly to my Cloudinary URL.
- I once again returned to my app created on Heroku and clicked on the Settings tab and revealed config vars. From here I added a key of CLOUDINARY_URL and the value of the API Environment Variable I copied from Cloudinary and I added this. Here I also added another Config Var with a key of DISABLE_COLLECTSTATIC with a value of 1. This was only added tempoarily and will be removed before deployment.
- Back in Gitpod in the settings.py file I added cloudinary and cloudinary_storage to INSTALLED_APPS. Here I also instructed Django to use Cloudinary to store media and static files. I also linked my file to the templates directory in Heroku using os.path.join. I also changed the TEMPLATES value to TEMPLATES_DIR in order to link them.
- I added my Heroku app name to the ALLOWED_HOSTS in the settings.py file also in the correct format. 
- In Gitpod I next created 3 folders in the top level directory of media, templates and static.
- Here I also created a file called Procfile. I added the following code to the Procfile web: gunicorn (timetopause).wsgi.
- I saved all my files. In the terminal I added my files to GitHub using git add ., git commit -m 'Deployment commit' and git push.
- From here I returned to my project in Heroku, I selected the Deploy tab, in the 'Deployment Method' I selected GitHub. In the textbox that appeared I entered my apps name as it appeared on GitHub confirmed it was the correct project. I scrolled down to the 'Manual Deploy' option and selected 'Deploy Branch'. I wacthed my build logs from here and selected to open the app once it was complete. 