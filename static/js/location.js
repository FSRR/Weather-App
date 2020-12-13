const ubicacion = document.getElementById('location')

function getLocation() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition)
    } else {
        alert('No es compatible con tu navegador')
    }
}

let loc

function showPosition(position) {
    console.log(position.coords.latitude)
    console.log(position.coords.longitude)
}

ubicacion.addEventListener('click', () => {
    getLocation()
})

