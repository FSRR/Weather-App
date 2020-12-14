const ubicacion = document.getElementById('location')
let loc

function getLocation() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition)
    } else {
        alert('No es compatible con tu navegador')
    }
}


function showPosition(position) {
    loc = `${position.coords.latitude},${position.coords.longitude}`
    return loc
}

ubicacion.addEventListener('click', () => {
    getLocation()

    let xhr
    if(XMLHttpRequest) xhr = new XMLHttpRequest()
    else xhr = new ActiveXObject()

    xhr.open('GET', `/${loc}`)

    xhr.send()
})

