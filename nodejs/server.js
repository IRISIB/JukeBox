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
  		playlist = message;
		playlistOnline = true;
        console.log('Manager says : ' + playlist);
		nsp_player.emit('playlistOn', playlist);
		nsp_voting.emit('playlistOn', playlist);
		current_trackId = JSON.parse(playlist).Tracks[0].DeezerId;
		nsp_player.emit('current_track', current_trackId);
		var votes_null = [];
		for(var index in JSON.parse(playlist).Tracks){
			console.log(index+": "+ JSON.parse(playlist).Tracks[index].title);
			votes_null.push(0);
		}
		votes = votes_null;
		console.log(votes);
		nsp_player.emit('votes', votes);
		
		setTimeout(reset, JSON.parse(playlist).Tracks[0].msec); 
		
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
      console.log(maxIndex + " : " + JSON.parse(playlist).Tracks[maxIndex].title 
      				+ " - msec : " + JSON.parse(playlist).Tracks[maxIndex].msec);
	  current_trackId = JSON.parse(playlist).Tracks[maxIndex].DeezerId;
	  /*
      var votes_null = [];
      for(var index in JSON.parse(playlist).Tracks){
        votes_null.push(0);
      }
	  votes = votes_null;
	  nsp_player.emit('votes', votes);
	  */
	  nsp_player.emit('current_track', current_trackId);
	  setTimeout(reset, JSON.parse(playlist).Tracks[maxIndex].msec);
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

//namespace par défaut
io.sockets.on('connection', function (socket) {
	socket.on('disconnect', function(){
    console.log('user disconnected');
	});
});

