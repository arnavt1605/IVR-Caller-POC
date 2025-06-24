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
  <li>Twilio <br>
  '''bash
  pip install twilio
  ''' <br>
  </li>
  
</ol>
