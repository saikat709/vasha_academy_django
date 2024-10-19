function toggleHide(a){
    document.querySelector(`#${a}`).classList.toggle('hidden')
}

window.addEventListener('load', function(e){

     const fileInput = document.getElementById('fileInput');
     const imagePreview = document.getElementById('userPhoto');

      fileInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        console.log("connected another log");
        if (file) {
            const url = reader.readAsDataURL(file);
            imagePreview.setAttr('src', url);
        } else {
            imagePreview.style.display = 'none';
        }
      });
});
