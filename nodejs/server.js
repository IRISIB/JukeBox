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
var votes = [];
var current_trackId;

var nsp_manager = io.of('/manager');
nsp_manager.on('connection', function(socket){
  console.log('Manager connected');
  socket.emit('connected', 'Hi Manager!');
  socket.on('playlistOn', function (message) {
        console.log('Manager says : ' + message);
        /*
		playlist = message;
		playlistOnline = true;
		nsp_player.emit('playlistOn', playlist);
		nsp_voting.emit('playlistOn', playlist);
		console.log(JSON.parse(playlist).Tracks[0].SpotifyId);
		current_trackId = JSON.parse(playlist).Tracks[0].SpotifyId;
		nsp_player.emit('current_track', current_trackId);
		var votes_null = [];
		for(var index in JSON.parse(playlist).Tracks){
			console.log(index+": "+ JSON.parse(playlist).Tracks[index].name);
			votes_null.push(0);
		}
		votes = votes_null;
		console.log(votes);
		nsp_player.emit('votes', votes);
		
		setTimeout(reset, 20000); */
		
    }); 
	
	socket.on('playlistOff', function (message) {
        console.log('Manager says : ' + message);
		playlist = message;
		playlistOnline = false;
		nsp_player.emit('playlistOff', playlist);
		nsp_voting.emit('playlistOff', playlist);
    }); 
	
});


function reset(){ 
	if(playlistOnline){
      var maxIndex = votes.indexOf(Math.max.apply(Math, votes));
      console.log(maxIndex + " : " + JSON.parse(playlist).Tracks[maxIndex].name);
	  current_trackId = JSON.parse(playlist).Tracks[maxIndex].SpotifyId;
      var votes_null = [];
      for(var index in JSON.parse(playlist).Tracks){
        votes_null.push(0);
      }
	  votes = votes_null;
	  nsp_player.emit('votes', votes);
	  nsp_player.emit('current_track', current_trackId);
	  setTimeout(reset, 20000);
	}
}

var nsp_player = io.of('/player');
nsp_player.on('connection', function(socket){
  console.log('Player connected');
  socket.emit('connected', 'Hi Player!');
  if(playlistOnline){
	socket.emit('playlistOn', playlist);
	socket.emit('votes', votes);
	socket.emit('current_track', current_trackId);
	}
  else{socket.emit('playlistOff', playlist);}
  
  
  //non nécessaire
  socket.on('reset', function (message) {
        console.log('Player says : ' + message);
		votes = message;
		console.log(votes);
		nsp_player.emit('votes', votes);
    }); 
	//non nécessaire
	socket.on('track', function (message) {
        console.log('Player says : ' + message);
		current_trackId = message;
		nsp_player.emit('current_track', current_trackId);
    }); 
  
});

var nsp_voting = io.of('/voting');
nsp_voting.on('connection', function(socket){
  console.log('Voting connected');
  socket.emit('connected', 'Hi Voting!');
  if(playlistOnline){socket.emit('playlistOn', playlist);}
  else{socket.emit('playlistOff', playlist);}
  
  socket.on('vote', function (message) {
        console.log('Voting says : ' + message);
		votes[message]++;
		console.log(votes);
		nsp_player.emit('votes', votes);
    }); 
  
});


io.sockets.on('connection', function (socket) {
	
	//clients.push(socket.id);
	//console.log('New user connected');
	
	socket.on('disconnect', function(){
    console.log('user disconnected');
	});
    // Dès qu'on reçoit un "message" (clic sur le bouton), on le note dans la console
    socket.on('message', function (message) {
        // On récupère le pseudo de celui qui a cliqué dans les variables de session
        console.log('Le Client me parle ! Il me dit : ' + message);
    }); 
});

