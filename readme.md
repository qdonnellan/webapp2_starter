# Webapp2 Starter Kit


The point of this project is to provide a starter kit for developers looking to deploy to Google App Engine in very little time. All you need to do to have your own webapp up and running is to:

1. Fork this repository
2. Change the application name in app.yaml
3. Deploy to Google App Engine

That's it!

## Test Driven
You've already got some baisc tests written, and it should be easy to add some more. Current tests can be found in the test folder. Install [Nose](https://nose.readthedocs.org/en/latest/) and then use it to test your app! 

**After you've forked this repo, cd to it from the terminal then run:**

    nosetests --with-gae --without-sandbox
  

## Templates (Jinja2)
Templates for this app can be found in the templates file under views

    /views
      /templates
          base.html
          front.html
          etc...
          
This webapp uses Jinja2 for a lightweight templating experience.

## CSS (Bootstrap)
Bootstrap is included in the base template as a link to the bootstrap CDN

    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css">
  
You may wish to customize your style on top of bootstrap, just edit the css file located your static css folder

    /public
      /static
        /css
          public.css
        
### Font Awesome Included
We've included a link to the font awesome CDN in the base template, so you can have fun including those icons from day 1

## Javascript/JQuery
JQuery is already included as a link to the Google CDN on the base template
  
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

You may wish to add your own javascript, just add your js scripts to the public-app.js file

    /public
      /static
        /js
          public-app.js

