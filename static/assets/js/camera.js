document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureButton = document.getElementById('capture');
    const imageContainer = document.getElementById('image-container');
    const context = canvas.getContext('2d');

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            console.error("Kamera xatosi: ", err);
        });

    captureButton.addEventListener('click', () => {
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const dataURL = canvas.toDataURL('image/png');
    
        fetch('/upload/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: dataURL })
        })
        .then(response => response.json())
        .then(data => {
            const imageElement = document.createElement('img');
            imageElement.src = data.image_url; // serverdan kelgan rasm URL sifatida
            imageContainer.appendChild(imageElement);
        })
        .catch((error) => {
            console.error('Xato:', error);
        });
    });
});
