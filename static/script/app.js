let trackListContainer = document.querySelector('.track-list-container');
let url;


// get all tracks
fetch('http://127.0.0.1:8000/json/songs/')
  .then(res => res.json())
  .then(data => {
    let songs = data;
    for (let song in songs){
      url = `http://127.0.0.1:8000/media/${songs[song].fields.song}`;
      
      let output = `
        <h1 id='song${[song]}' class='song-pk'>${songs[song].pk}</h1>
      `;
      trackListContainer.innerHTML += output;
      
    }

    for(let song in songs){
      let songPk = document.querySelector(`#song${[song]}`)
      // get single track
      songPk.addEventListener('click', e => {
        trackListContainer.innerHTML = "";
        fetch(`http://127.0.0.1:8000/json/song/${songs[song].pk}/`)
        .then(res => res.json())
        .then(data => {
          let song = data;
          console.log(song)
          url = `http://127.0.0.1:8000/media/${song[0].fields.song}`;
          trackListContainer.innerHTML += `
            <audio controls autoplay src='${url}'></audio>
          `
        })
        .catch(error => console.log(error))
      })      
    }
  })
  .catch(error => console.log(error))


