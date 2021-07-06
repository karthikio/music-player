let trackListContainer = document.querySelector('.track-list-container');
let songContainer = document.querySelector('.song-container');
let audioPlayer = document.querySelector('#audio-player')
let url;

// controls
let nextBtn = document.getElementById('next-btn')
let previousBtn = document.getElementById('previous-btn')
let repeatBtn = document.getElementById('repeat-btn')

// song index
let songIndex = 0;

let list;

// get all tracks
fetch('http://127.0.0.1:8000/json/songs/')
  .then(res => res.json())
  .then(data => {
    let songs = data;
    for (let song in songs){
      url = `http://127.0.0.1:8000/media/${songs[song].fields.song}`;
      
      let output = `
        <div  class='song-name' id='song${[song]}'>
          <p>${songs[song].fields.name}</p>
        </div>
      `;
      trackListContainer.innerHTML += output;
      
    }

    for(let song in songs){
      let songName = document.querySelector(`#song${[song]}`)
      // get single track
      songName.addEventListener('click', e => {
        fetch(`http://127.0.0.1:8000/json/song/${songs[song].pk}/`)
        .then(res => res.json())
        .then(data => {
          let song = data;
          
          listIndex = song[0].fields.song;

          url = `http://127.0.0.1:8000/media/${listIndex}`;
          let outputSong = `
            <audio id="audio-player" controls autoplay src='${url}'></audio>
          `;
          songContainer.innerHTML = outputSong;

          nextBtn.addEventListener('click', ()=>{
            nextSong();
          })
      
        })
        .catch(error => console.log(error))
      })      
    }
  })
  .catch(error => console.log(error))


//load song 
function loadSong(listIndex, index){
  console.log(audioPlayer)
}

//next song
function nextSong() {
  songIndex++;

  loadSong(listIndex, songIndex);
}



//next song
function nextSong() {
  songIndex++;
  // we have used -1, cause index starts for zero
  if (songIndex > (list.length - 1)) {
    songIndex = 0;
  }

  loadSong(list[songIndex], songIndex);
}

//previous song
function previousSong(){
  // checking positive or negative
  if (songIndex > 0) {
    songIndex--;
  }else{
    songIndex=0;
  }

  loadSong(list[songIndex], songIndex);
}

//repeat song
function repeatSong(){
  if(repeatBtn.className === "loop-false"){
    audioPlayer.loop = true;
    repeatBtn.className = "loop-true";
    console.log(songIndex)

  }else{
    audioPlayer.loop = false;
    repeatBtn.className = "loop-false";
    console.log(songIndex)

  }
}

// auto next song 
audioPlayer.addEventListener('ended',()=>{
  // need changes//////////////////////////////
  if(songIndex > (list.length -1)){
    audioPlayer.pause = true;
  }else{
    nextSong();
  }
})

