// CS Project 4485
// Virtual TA Project
// Team 9 - Anjum Chida

var sendForm = document.querySelector('#chatform'),
    textInput = document.querySelector('.chatbox'),
    chatList = document.querySelector('.chatlist'),
    userBubble = document.querySelectorAll('.userInput'),
    botBubble = document.querySelectorAll('.bot__output'),
    animateBotBubble = document.querySelectorAll('.bot__input--animation'),
    overview = document.querySelector('.chatbot__overview'),
    hasCorrectInput,
    imgLoader = false,
    animationCounter = 1,
    animationBubbleDelay = 600,
    input,
    previousInput,
    isReaction = false,
    unkwnCommReaction = "I didn't quite get that.",
    chatbotButton = document.querySelector(".submit-button")

sendForm.onkeydown = function(e)
{

  if(e.keyCode == 13)
  {
    e.preventDefault();
    var input = textInput.value.toLowerCase();
    if(input.length > 0)
    {
      let xhr = new XMLHttpRequest();
      xhr.open('POST', '/index.html');
      //xhr.setRequestHeader('Content-type', 'application/json');
      xhr.setRequestHeader('chatbox', input);
      xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
         console.log(xhr.status);
         console.log(xhr.response);
         unknownCommand(xhr.response);
      }};
      createBubble(input)
      xhr.send();
    }
  }
};

sendForm.addEventListener('submit', function(e)
{
  //so form doesnt submit page (no page refresh)
  e.preventDefault();
  //No mix ups with upper and lowercases
  var input = textInput.value.toLowerCase();
  if(input.length > 0)
  {
      let xhr = new XMLHttpRequest();
      xhr.open('POST', '/index.html');

      //xhr.setRequestHeader('Content-type', 'application/json');
      xhr.setRequestHeader('chatbox', input);
      xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
         console.log(xhr.status);
         console.log(xhr.response);
         unknownCommand(xhr.response);
      }};
      createBubble(input)

      xhr.send();
  }
})

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

document.getElementById('myBtn').addEventListener("click", function()
{
  modal.style.display = "block";
});

// When the user clicks on <span> (x), close the modal
span.onclick = function()
{
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event)
{
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
var createBubble = function(input)
{
  //create input bubble
  var chatBubble = document.createElement('li');
  chatBubble.classList.add('userInput');

  //adds input of textarea to chatbubble list item
  chatBubble.innerHTML = input;

  //adds chatBubble to chatlist
  chatList.appendChild(chatBubble)

  //botResponse(input);
  //checkInput(input);
}

var checkInput = function(input)
{
  hasCorrectInput = false;
  isReaction = false;
  //Checks all text values in possibleInput
  /*
  for(var textVal in possibleInput)
  {
    //If user reacts with "yes" and the previous input was in textVal
    if(input == "yes" || input.indexOf("yes") >= 0)
    {
      if(previousInput == textVal)
      {
        console.log("sausigheid");

        isReaction = true;
        hasCorrectInput = true;
        botResponse(textVal);
      }
    }
    if(input == "no" && previousInput == textVal)
    {
      unkwnCommReaction = "For a list of commands type: Commands";
      unknownCommand("I'm sorry to hear that :(")
      unknownCommand(unkwnCommReaction);
      hasCorrectInput = true;
    }
    //Is a word of the input also in possibleInput object?
    if(input == textVal || input.indexOf(textVal) >=0 && isReaction == false)
    {
			console.log("succes");
      hasCorrectInput = true;
      botResponse(textVal);
		}
  }*/
  //When input is not in possibleInput
  if(hasCorrectInput == false)
  {
    console.log("failed");
    unknownCommand(unkwnCommReaction);
    hasCorrectInput = true;
  }
}

function buttonClick()
{
  document.getElementById("type_box").innerHTML = '$$\\sum\\limits$$'
  MathJax.Hub.Queue(["Typeset",MathJax.Hub,"type_box"]);
}

function botResponse(textVal)
{
  //create response bubble
  var userBubble = document.createElement('li');
  userBubble.classList.add('bot__output');

  if(isReaction == true)
  {
    if (typeof reactionInput[textVal] === "function")
    {
    //adds input of textarea to chatbubble list item
      userBubble.innerHTML = textVal;
    } 
    else
    {
      userBubble.innerHTML = textVal;
    }
  }

  if(isReaction == false)
  {
    if (typeof possibleInput[textVal] === "function")
    {
      userBubble.innerHTML = textVal;
    }
    else 
    {
      userBubble.innerHTML = textVal;
    }
  }
}

function unknownCommand(unkwnCommReaction)
{
  //create response bubble
  var failedResponse = document.createElement('li');

  failedResponse.classList.add('bot__output');
  failedResponse.classList.add('bot__output--failed');

  //Add text to failedResponse
  failedResponse.innerHTML = unkwnCommReaction; //adds input of textarea to chatbubble list item

  //add list item to chatlist
  chatList.appendChild(failedResponse) //adds chatBubble to chatlist

  animateBotOutput();

  // reset text area input
  textInput.value = "";

  //Sets chatlist scroll to bottom
  chatList.scrollTop = chatList.scrollHeight;

  animationCounter = 1;
}
function summation()
{
  document.getElementById("type_box").textContent += '\u2211';
}
function squareRoot()
{
  document.getElementById("type_box").textContent += '\u221A';
}
function forall()
{
  document.getElementById("type_box").textContent += '\u2200';
}
function exist()
{
  document.getElementById("type_box").textContent += '\u2203';
}
function isin()
{
  document.getElementById("type_box").textContent += '\u2208';
}
function cap()
{
  document.getElementById("type_box").textContent += '\u2229';
}
function cup()
{
  document.getElementById("type_box").textContent += '\u222A';
}
function Lambda()
{
  document.getElementById("type_box").textContent += '\u039B';
}
function lambda()
{
  document.getElementById("type_box").textContent += '\u03BB';
}
function Omicron()
{
  document.getElementById("type_box").textContent += '\u039F';
}
function omicron()
{
  document.getElementById("type_box").textContent += '\u03BF';
}
function Theta()
{
  document.getElementById("type_box").textContent += '\u0398';
}
function theta()
{
  document.getElementById("type_box").textContent += '\u03B8';
}
function Omega()
{
  document.getElementById("type_box").textContent += '\u03A9';
}
function omega()
{
  document.getElementById("type_box").textContent += '\u03C9';
}
function responseText(e)
{
  var response = document.createElement('li');
  response.classList.add('bot__output');
  response.innerHTML = e;

  chatList.appendChild(response);

  animateBotOutput();

  console.log(response.clientHeight);

  //Sets chatlist scroll to bottom
  setTimeout(function()
  {
    chatList.scrollTop = chatList.scrollHeight;
    console.log(response.clientHeight);
  }, 0)
}

function responseImg(e)
{
  var image = new Image();
  image.classList.add('bot__output');
  //Custom class for styling
  image.classList.add('bot__outputImage');
  //Gets the image
  image.src = "/images/"+e;
  chatList.appendChild(image);

  animateBotOutput()

  if(image.completed)
  {
    chatList.scrollTop = chatList.scrollTop + image.scrollHeight;
  }
  else 
  {
    image.addEventListener('load', function()
    {
      chatList.scrollTop = chatList.scrollTop + image.scrollHeight;
    })
  }
}

//change to SCSS loop
function animateBotOutput() 
{
  chatList.lastElementChild.style.animationDelay= (animationCounter * animationBubbleDelay)+"ms";
  animationCounter++;
  chatList.lastElementChild.style.animationPlayState = "running";
}

function commandReset(e)
{
  animationCounter = 1;
  previousInput = Object.keys(possibleInput)[e];
}

var possibleInput = {}
var reactionInput = {}
