function toggleHide(a){
    document.querySelector(`#${a}`).classList.toggle('hidden')
}

window.addEventListener('load', function(e){
    console.log("connected log")
});

console.log("connected another log")