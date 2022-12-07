# Music Match
 
Music Match is a web application that assists users in finding new songs to listen to. This is my documentation for Music Match.

Youtube video link:
 
# To Get Started
 
Check if you have pip by heading to your terminal and running <br/>
`pip --version` <br/>
If pip is not installed, you will get an error that looks like "pip not found". Install pip using [Online Guide](https://www.geeksforgeeks.org/download-and-install-pip-latest-version/) <br/>
 
### Make sure you are in the musicproject folder
 
Execute: <br/>
`pip install -r requirements.txt`
 
# To Run Flask
 
### Make sure you are in the MusicMatch folder
 
To run our application in Flask, execute these three lines: <br/>
 
`export FLASK_APP=musicproject` <br/>
`export FLASK_ENV=development` <br/>
`flask run`

# Navigating Music Match
After 'flask run,' flask should be up and running! In the terminal, just find the port running flask: the port typically looks like http://127.0.0.1:5000. Copy the port address, and open it as a url in any browser. Now, you can access and interact with the web application. Welcome to Music Match!

## Making your account and logging in
Now, you should make an account within Music Match. Please Navigate to the top right hand corner of the page. Here, on the left hand side of “Login” you should find “Register”, click on "Register". Now, you will be presented with a signup form which includes First Name, Last Name, Email, Username, Password, and Re-type Password fields. Each field has been labeled so just input what each field requests in order to register. Once properly registering, you will be redirected a login page requesting a username and password. Now, all you have to do is login with the credentials of the account you just made. Click "Log In" and now you've officially entered Music Match!

## Home page and profile
After logging in, you are directed to the home page, which provides instructions for the two main uses of Music Match. Along the top of the page, you have three main options to venture to. Starting off, we will visit the profile. Navigating to the top right hand side of the page, to the left of "Logout", you'll see "Profile". Click on "Profile", and you'll be brough to a page displaying all the information (First Name, Last Name, Email, Username) you inputted relating to your account.

## The Recommender
Now, I think you want to see the actual function of the web app. Let's say you want to be recommended some music. From the profile page, you still have access to the the black navagation bar along the top of your screen. From here, navigate to the top left corner of the page. Here, to the right of "MUSIC MATCH," you'll find "Recommender", click on it. On this page, you can be recommended a song by first inputting a song that you like. You can do this by entering a song's name and artist in the respectively labeled fields. Make sure you use and spell the full name of the song and artist or else you may be inputting the wrong song! Hit the blue "Submit" button, and you should be directed to your resulting song recommendation. Here, you'll see the album cover of the song we recommended along with the name and artist. Don't like this song? No worries! Just refresh the page to get a new recommendation from the same song (if there are enough similar songs left), or navigate back to the top left of the page and hit "Recommender" to input a new song.

## The Sentencer
Now, let's say you're looking for a more random selection of songs. The sentencer is perfect for you! From the recommender, navigate to the top left corner of the page again, and to the right of "Recommender," you'll find "Sentencer," click on it. Here, you'll see an input box requesting a sentence. Enter any sentence, and hit convert. Now, you'll be given a song for each word that contains the word in the title. Want to do it again? Just navigate back to the top of the page, hit "Sentencer" in the black navigation bar, and type in a new sentence!

Finished with Music Match? To log out, just click “Log Out” in the top right corner of the screen. Not quite finished? To navigate back to the home page, hit the green MUSIC MATCH logo in the top left corner. To go back to the Sentencer, Recommender, or Profile, just click their respective links in the black navigation bar.