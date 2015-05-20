var SCROLLER_LENGTH = 18;
var HEIGHT = 7;

function clearLights(){
  var lightsOn = $('.on');
  lightsOn.addClass('off');
  lightsOn.removeClass('on');
}

function setLight(row, col, state){
  var theLight = $('.'+row+'_'+col);
  
  if(theLight.hasClass('on') && !state){
    theLight.removeClass('on');
    theLight.addClass('off');
  }else if(theLight.hasClass('off') && state){
    theLight.removeClass('off');
    theLight.addClass('on');
  }
}

function drawMessage(messageArray, leftPointer){
  var messageLength = messageArray.length;
  var total<a href="http://www.jqueryscript.net/tags.php?/Scroll/">Scroll</a>Length = SCROLLER_LENGTH + messageLength;
  
  if(messageLength>0){
    
    for(var col=0;col<messageLength;col++){
      for(var row=0;row<HEIGHT;row++){
        var offsetCol = leftPointer + col;
        
        if(offsetCol<SCROLLER_LENGTH || offsetCol >= 0){
          setLight(row,offsetCol,messageArray[col][row]);
        }
        
      }
    }
    
  }
}

function textToLED(theWord){
  var theMessage = [];
  theWord = theWord.toUpperCase();
  for(var i=0;i<theWord.length;i++){
    theMessage.push(charToLED(theWord.charAt(i)));
    theMessage.push(charToLED());
  }
  
  var flatten = [];
  flatten = flatten.concat.apply(flatten, theMessage);
  
  return flatten;
}

function charToLED(theChar){
  var theLed = [];
  switch(theChar){
    case 'A' :
      theLed = [[false, false, true, true, true, true, true], 
        [false, true, false, false, true, false, false], 
        [true, false, false, false, true, false, false],
        [false, true, false, false, true, false, false],
        [false, false, true, true, true, true, true]];
      break;
    case 'B' :
      theLed = [[true, true, true, true, true, true, true], 
        [true, false, false, true, false, false, true],
        [true, false, false, true, false, false, true],
        [true, false, false, true, false, false, true],
        [false, true, true, false, true, true, false]];
      break;
    case 'C' :
      theLed = [[false, true, true, true, true, true, false], 
        [true, false, false, false, false, false, true],
        [true, false, false, false, false, false, true],
        [true, false, false, false, false, false, true],
        [false, true, false, false, false, true, false]]; 
      break;
     case 'D' :
      theLed = [[true, true, true, true, true, true, true], 
        [true, false, false, false, false, false, true],
        [true, false, false, false, false, false, true],
        [true, false, false, false, false, false, true],
        [false, true, true, true, true, true, false]]; 
      break;
    case 'E' :
      theLed = [[true, true, true, true, true, true, true], 
        [true, false, false, true, false, false, true],
        [true, false, false, true, false, false, true],
        [true, false, false, true, false, false, true],
        [true, false, false, false, false, false, true]];
      break;
    case 'F' :
      theLed = [[true, true, true, true, true, true, true], 
        [true, false, false, true, false, false, false],
        [true, false, false, true, false, false, false],
        [true, false, false, true, false, false, false],
        [true, false, false, false, false, false, false]];
      break;
    case 'G' :
      theLed = [[false, true, true, true, true, true, false], 
        [true, false, false, false, false, false, true],
        [true, false, false, false, false, false, true],
        [true, false, false, false, true, false, true],
        [true, true, false, false, true, true, true]];
      break;
    case 'H' :
      theLed = [[true, true, true, true, true, true, true], 
        [false, false, false, true, false, false, false],
        [false, false, false, true, false, false, false],
        [false, false, false, true, false, false, false],
        [true, true, true, true, true, true, true]];
      break;
    case 'I' :
      theLed = [[false, false, false, false, false, false, false], 
        [true, false, false, false, false, false, true],
        [true, true, true, true, true, true, true],
        [true, false, false, false, false, false, true],
        [false, false, false, false, false, false, false]];
      break;
    case 'J' :
      theLed = [[false, false, false, false, false, true, false], 
        [false, false, false, false, false, false, true],
        [true, false, false, false, false, false, true],
        [true, true, true, true, true, true, false],
        [true, false, false, false, false, false, false]];
      break;  
   case 'K' :
      theLed = [[true, true, true, true, true, true, true], 
        [false, false, false, true, false, false, false],
        [false, false, true, false, true, false, false],
        [false, true, false, false, false, true, false],
        [true, false, false, false, false, false, true]];
      break;
   case 'L' :
      theLed = [[true, true, true, true, true, true, true], 
        [false, false, false, false, false, false, true],
        [false, false, false, false, false, false, true],
        [false, false, false, false, false, false, true],
        [false, false, false, false, false, false, true]];
      break;
   case 'M' :
      theLed = [[true, true, true, true, true, true, true], 
        [false, true, false, false, false, false, false],
        [false, false, true, false, false, false, false],
        [false, true, false, false, false, false, false],
        [true, true, true, true, true, true, true]];
      break;
   case 'N' :
      theLed = [[true, true, true, true, true, true, true], 
        [false, false, true, false, false, false, false],
        [false, false, false, true, false, false, false],
        [false, false, false, false, true, false, false],
        [true, true, true, true, true, true, true]];
      break;
   case 'O' :
      theLed = [[false, true, true, true, true, true, false], 
        [true, false, false, false, false, false, true],
        [true, false, false, false, false, false, true],
        [true, false, false, false, false, false, true],
        [false, true, true, true, true, true, false]];
      break;
   case 'P' :
      theLed = [[true, true, true, true, true, true, true], 
        [true, false, false, true, false, false, false],
        [true, false, false, true, false, false, false],
        [true, false, false, true, false, false, false],
        [false, true, true, false, false, false, false]];
      break;
   case 'Q' :
      theLed = [[false, true, true, true, true, true, false], 
        [true, false, false, false, false, false, true],
        [true, false, false, false, true, false, true],
        [true, false, false, false, false, true, false],
        [false, true, true, true, true, false, true]];
      break;
   case 'R' :
      theLed = [[true, true, true, true, true, true, true], 
        [true, false, false, true, false, false, false],
        [true, false, false, true, false, false, false],
        [true, false, false, true, false, false, false],
        [false, true, true, false, true, true, true]];
      break;
   case 'S' :
      theLed = [[false, true, true, false, false, false, true], 
        [true, false, false, true, false, false, true],
        [true, false, false, true, false, false, true],
        [true, false, false, true, false, false, true],
        [true, false, false, false, true, true, false]];
      break;
   case 'T' :
      theLed = [[true, false, false, false, false, false, false], 
        [true, false, false, false, false, false, false],
        [true, true, true, true, true, true, true],
        [true, false, false, false, false, false, false],
        [true, false, false, false, false, false, false]];
      break;
   case 'U' :
      theLed = [[true, true, true, true, true, true, false], 
        [false, false, false, false, false, false, true],
        [false, false, false, false, false, false, true],
        [false, false, false, false, false, false, true],
        [true, true, true, true, true, true, false]];
      break;
   case 'V' :
      theLed = [[true, true, true, true, true, false, false], 
        [false, false, false, false, false, true, false],
        [false, false, false, false, false, false, true],
        [false, false, false, false, false, true, false],
        [true, true, true, true, true, false, false]];
      break;
   case 'W' :
      theLed = [[true, true, true, true, true, true, false], 
        [false, false, false, false, false, false, true],
        [false, false, false, false, true, true, false],
        [false, false, false, false, false, false, true],
        [true, true, true, true, true, true, false]];
      break;
   case 'X' :
      theLed = [[true, false, false, false, false, false, true], 
        [false, true, true, false, true, true, false],
        [false, false, false, true, false, false, false],
        [false, true, true, false, true, true, false],
        [true, false, false, false, false, false, true]];
      break;
   case 'Y' :
      theLed = [[true, false, false, false, false, false, false], 
        [false, true, false, false, false, false, false],
        [false, false, true, true, true, true, true],
        [false, true, false, false, false, false, false],
        [true, false, false, false, false, false, false]];
      break;
   case 'Z' :
      theLed = [[true, false, false, false, false, true, true], 
        [true, false, false, false, true, false, true],
        [true, false, false, true, false, false, true],
        [true, false, true, false, false, false, true],
        [true, true, false, false, false, false, true]];
      break;
    default:
      theLed = [[false, false, false, false, false, false, false]];
  }  
  return theLed;
}

var fps = 30;

// The message you wish to display
var myMessage = textToLED('jQuery Script Net');
var leftPointer = SCROLLER_LENGTH + 1;
var rightPointer = 0;
var furthestLeftPoint = 0 - myMessage.length;

function draw() {
  setTimeout(function() {
    request<a href="http://www.jqueryscript.net/animation/">Animation</a>Frame(draw);
      clearLights();
    
      if(leftPointer==furthestLeftPoint){
        leftPointer = SCROLLER_LENGTH + 1;
      }
    
      drawMessage(myMessage, leftPointer);
      leftPointer--;     
      
    }, 1000 / fps);
}

draw();