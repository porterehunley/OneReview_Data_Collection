function getTitlesByYear(year) {	
	fetch('http://127.0.0.1:5000/titles/' + year.toString(10))
	  .then(function(response) {
	    return response.json();
	  })
	  .then(function(myJson) {
	    myJson.titles.forEach(function(title) {
	    	addToList(title.toString());
	    });
	    return "Media_List";
	  })
	  .then(function(listId) {
	  	highlightFirstListElement(listId);
	  	return "Media_List";
	  })
	  .then(function(listId) {
	  	getFirstItemFromList(listId);
	  });
}

function main_pipeline() {
	fetch('http://127.0.0.1:5000/titles/' + year.toString(10))
	  .then(function(response) {
	    return response.json();
	  })
	  .then(function(myJson) {
	    myJson.titles.forEach(function(title) {
	    	addToList(title.toString());
	    });
	    return "Media_List";
	  })
	  .then();
}


function addToList(title) {
	var listItem = document.createElement("LI");
	var textItem = document.createTextNode(title);
	listItem.appendChild(textItem);
	listItem.className = "list-group-item";
	document.getElementById("Media_List").appendChild(listItem);
}

function getFirstItemFromList(listId) {
	var listElement = document.getElementById(listId).firstElementChild.innerHTML;
	return listElement;
}
//Broken
function highlightFirstListElement(listId) {
	var listElement = document.getElementById("Media_List").firstElementChild;
	listElement.className = "list-group-item active";
}

function removeFirstListElement(listId) {
	var list = document.getElementById(listId);
	list.removeChild(list.childNodes[0]);
}

function updateMedia(title) {
	document.getElementById('Current_Media').innerHTML = 'Current Movie: ' + title;
}

function helloWorld() {
	console.log("Hello World!");
}