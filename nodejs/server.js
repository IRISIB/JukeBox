var http = require("http");
httpServer = http.createServer()
httpServer.listen(8888);
console.log('listening on *:8888');
var io = require('socket.io').listen(httpServer);
// io.sockets.on('connection', function (socket) {
   // socket.emit('connected', 'Connexion ok bis');
// });

//var clients = [];

var playlist = "Aucune playlist n'a été mise en ligne"; 
var playlistOnline = false;
var votes;
var current_track;
var limit;
var request = require("request")
var url = "http://0.0.0.0:8000/manager/getSession/"
var session = "plop";
var cnt = 0;

var nsp_manager = io.of('/manager');
nsp_manager.on('connection', function(socket){
  console.log('Manager connected');
  socket.emit('connected', 'Hi Manager!');
  socket.on('playlistOn', function (message) {

	// getJSON(url, function (body) {
	//   console.log('we have the body!', body);
 //  	  console.log(session, cnt); // Print the json response
	//   session = body;
	//   cnt = cnt + 1;
 //  	  console.log(session, cnt); // Print the json response
	// });
  	  	console.log(session, cnt); // Print the json response
  		limit = 5;
        console.log('Manager says : ' + session.playlist.title);
		playlistOnline = true;
		nsp_player.emit('playlistOn', session);
		nsp_voting.emit('playlistOn', session);
		current_track = session.current_track;
		nsp_player.emit('current_track', session);
		for(var index in session.tracks){
			console.log(index+": "+ session.tracks[index].title);
		}
		
    }); 
	
	socket.on('playlistOff', function (message) {
        console.log('Manager says : ' + message);
		playlist = message;
		playlistOnline = false;
		nsp_player.emit('playlistOff', playlist);
		nsp_voting.emit('playlistOff', playlist);
    }); 
	
});

function getJSON(url, callback) {
  request({
    url: url,
    json: true
  }, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      callback(body);
    }
  });
}

function limitedPlaylist(playlist, limit){
	var newPlaylist = playlist;
	var newPlaylistJSon = JSON.parse(newPlaylist);
	for(var index in newPlaylistJSon.Tracks){
			newPlaylistJSon.Tracks.splice(0, newPlaylistJSon.Tracks.length);
		}
		console.log(newPlaylistJSon);
	for(var i = 0, l = limit; i < l; i++) {
          	newPlaylistJSon.Tracks.push(JSON.parse(playlist).Tracks[i]);
        }
        console.log(newPlaylistJSon);
     newPlaylist = JSON.stringify(newPlaylistJSon);
    return newPlaylist;
}

function reset(){ 
	if(playlistOnline){
      var maxIndex = votes.indexOf(Math.max.apply(Math, votes));
      console.log(maxIndex + " : " + JSON.parse(playlist).Tracks[maxIndex].title 
      				+ " - msec : " + JSON.parse(playlist).Tracks[maxIndex].msec);
	  current_track = JSON.parse(playlist).Tracks[maxIndex];
	  nsp_player.emit('current_track', current_track);
	  setTimeout(reset, JSON.parse(playlist).Tracks[maxIndex].msec);
	}
}

var nsp_player = io.of('/player');
nsp_player.on('connection', function(socket){
  console.log('Player connected');
  socket.emit('connected', 'Hi Player!');
  if(playlistOnline){
	socket.emit('playlistOn', session);
	}
  else{socket.emit('playlistOff', playlist);}
  
});

var nsp_voting = io.of('/voting');
nsp_voting.on('connection', function(socket){
  console.log('Voting connected');
  socket.emit('connected', 'Hi Voting!');
  if(playlistOnline){socket.emit('playlistOn', session);}
  else{socket.emit('playlistOff', playlist);}
  
  socket.on('vote', function (message) {
        console.log('Voting says : ' + message);
        for (var i = session.tracks.length - 1; i >= 0; i--) {
        	if (session.tracks[i].DeezerId == message) {
	        	session.tracks[i].vote++;
        	};
        };
		nsp_player.emit('votes', session, message);
    
    }); 
  
});

//namespace par défaut
io.sockets.on('connection', function (socket) {
	socket.on('disconnect', function(){
    console.log('user disconnected');
	});
});


var request = require("request")

var url = "http://0.0.0.0:8000/manager/getSession/"

request({
    url: url,
    json: true
}, function (error, response, body) {

    if (!error && response.statusCode === 200) {
        console.log(body) // Print the json response
        console.log('Manager says : ' + body.playlist.title)
        session = body
    }
})

