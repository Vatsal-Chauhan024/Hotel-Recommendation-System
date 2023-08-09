var pos = 0;
//number of slides
var totalSlides = $('#slider-wrap ul li').length;
//get the slide width
var sliderWidth = $('#slider-wrap').width();

$(document).ready(function(){
	/*BUILD THE SLIDER*/
	//set width to be 'x' times the number of slides
	$('#slider-wrap ul#slider').width(sliderWidth*totalSlides);
    //next slide 	
	$('#next').click(function(){
		slideRight();
	});
	//previous slide
	$('#previous').click(function(){
		slideLeft();
	});
	//automatic slider
	var autoSlider = setInterval(slideRight, 2000);
	//for each slide 
	$.each($('#slider-wrap ul li'), function() { 
	   //create a pagination
	   var li = document.createElement('li');
	   $('#pagination-wrap ul').append(li);	   
	});
	//counter
	countSlides();
	//pagination
	pagination();
	//hide/show controls/btns when hover
	//pause automatic slide when hover
	$('#slider-wrap').hover(
	  function(){ $(this).addClass('active'); clearInterval(autoSlider); }, 
	  function(){ $(this).removeClass('active'); autoSlider = setInterval(slideRight, 3000); }
	);
});

/*SLIDE LEFT*/
function slideLeft(){
	pos--;
	if(pos==-1){ pos = totalSlides-1; }
	$('#slider-wrap ul#slider').css('left', -(sliderWidth*pos)); 	
	countSlides();
	pagination();
}

/*SLIDE RIGHT*/
function slideRight(){
	pos++;
	if(pos==totalSlides){ pos = 0; }
	$('#slider-wrap ul#slider').css('left', -(sliderWidth*pos)); 
	countSlides();
	pagination();
}

function countSlides(){
	$('#counter').html(pos+1 + ' / ' + totalSlides);
}

function pagination(){
	$('#pagination-wrap ul li').removeClass('active');
	$('#pagination-wrap ul li:eq('+pos+')').addClass('active');
}

const chat = document.getElementById("chatbot-chat");


$("#chatbot-open-container").click(function(){
  $("#open-chat-button").toggle(200);
  $("#close-chat-button").toggle(200);
  $("#chatbot-container").fadeToggle(200);
});

document.getElementById("chatbot-new-message-send-button").addEventListener("click", newInput);

document.getElementById("chatbot-input").addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      newInput();
    }
});

function newInput(){
  newText = document.getElementById("chatbot-input").value;
  if (newText != ""){
    document.getElementById("chatbot-input").value = "";
    addMessage("sent", newText);
    generateResponse(newText);
  }
}


function addMessage(type, text){
  let messageDiv = document.createElement("div");
  let responseText = document.createElement("p");
  responseText.appendChild(document.createTextNode(text));
  
  if (type == "sent"){
    messageDiv.classList.add("chatbot-messages", "chatbot-sent-messages");
  } else if (type == "received"){
    messageDiv.classList.add("chatbot-messages", "chatbot-received-messages");
  }

  messageDiv.appendChild(responseText);
  chat.prepend(messageDiv);
}




function generateResponse(prompt){
  // Here you can add your answer-generating code
  addMessage("received", "Great to hear that!");
}