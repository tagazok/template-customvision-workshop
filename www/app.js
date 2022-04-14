const resultDOM = document.querySelector('#result');
const rawResultDOM = document.querySelector('#raw-result');
document.querySelector('#fileUpload').addEventListener('change', callApi);
const imageDOM = document.querySelector('#image');

async function callApi() {
    const file = this.files[0];
    imageDOM.src = URL.createObjectURL(file);

    let formData = new FormData();
    formData.set('file', file);

    const payload = await fetch('/api/dogs', {
        method: 'POST',
        body: formData,
    });
    const data = await payload.json();
    console.log(data.predictions);
    resultDOM.textContent = data.predictions[0].tagName;
    rawResultDOM.textContent = JSON.stringify(data.predictions, undefined, 2);
}