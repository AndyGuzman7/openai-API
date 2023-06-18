
let mediaRecorder = null;
let btnStart, btnStop, audioPlay, textTranscription, grabar, cargando;
let dataArray = [];

let startRecording = () => {
    grabar.style.display = 'block';
    navigator.mediaDevices.getUserMedia({ audio: true }).then((mediaStreamObject) => {
        mediaRecorder = new MediaRecorder(mediaStreamObject, {mimeType: "audio/webm"});
        mediaRecorder.start();

        mediaRecorder.ondataavailable = (ev) => {
            dataArray.push(ev.data);
        };
    


    }).catch((err) => {
        console.log(err.name, err.message);
    });
}

let stopRecording = () => {
    let mimeType = mediaRecorder.mimeType;
    mediaRecorder.stop();
    cargando.style.display = 'block';
    grabar.style.display = 'none';

    mediaRecorder.onstop = (ev) => {
        let audioData = new Blob(dataArray, { 'type': mimeType });
        let audioSrc = window.URL.createObjectURL(audioData);

        dataArray = [];

        audioPlay.src = audioSrc;
        audioPlay.play();

        //textTranscription.innerHTML = 'Awaiting result...';

        let reader = new FileReader();
        reader.readAsDataURL(audioData);
        reader.onloadend = async () => {
            let base64audio = reader.result.split('base64,')[1];
            console.log(reader.result);
            let result = await axios.post('/transcribe', {
                data: base64audio
            });
            cargando.style.display = 'none';
            textTranscription.innerHTML = result.data.text;
        }
    };

    mediaRecorder = null;
}

window.onload = function() {
    btnStart = document.getElementById('btnStart');
    btnStop = document.getElementById('btnStop');
    audioPlay = document.getElementById('audioPlay');
    textTranscription = document.getElementById('textTranscription');
    grabar = document.getElementById('grabar')
    document.getElementById('grabar').style.display = 'none';

    cargando = document.getElementById('cargando')
    document.getElementById('cargando').style.display = 'none';

    btnStart.addEventListener('click', startRecording);
    btnStop.addEventListener('click', stopRecording);
}

