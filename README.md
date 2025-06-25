<h1>IVR Caller POC</h1>
<p>Implemented a simple proof of concept for an IVR system using Python, Flask, Twilio and ngrok.</p>

<p>A phone number is automatically called and a message is played followed by taking input from the user.</p>

<h3>Working Procedure</h3>
<ol>
  <li>Run a Flask server to serve the TwiML instructions</li>
  <li>Ngrok is used to expose the local server to the internet</li>
  <li>Twilio provided number is used to make a phone call to a desired number</li>
  <li>User can listen to messages and give inputs through the numpad</li>
</ol>

<h3>Requirements</h3>
<ol>
  <li>Python </li>
  <li>Twilio - pip install twilio </li>
  <li>Flask - pip install flask</li>
  <li>ngrok - choco install ngrok</li>
</ol>

<h3>Steps to Run</h3>
<ol>
  <li>Clone the repository and install dependencies</li>
  <li>Run the flask server using command - python app.py</li>
  <li>Run the command while your flask server is running - ngrok http 5000</li>
  <li>Copy the url show by ngrok</li>
  <li>In call.py, update your Account ID and Authentication Token along with the respective to and from phone numbers and ngrok url</li>
  <li>Run the call script call.py</li>
</ol>

<p>Following the above steps will successfully initiate the call.</p>

<h3>Caution</h3>
<p>Run call.py only after making sure that both Flask code and ngrok server are up and running. Otherwise you will definitely get errors.</p>
