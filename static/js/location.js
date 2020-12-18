const ubicacion = document.getElementById('location')
let loc

function getLocation() {
    if (navigator.geolocation) navigator.geolocation.getCurrentPosition(showPosition)
    else alert('No es compatible con tu navegador')
}


function showPosition(position) {
    loc = `${position.coords.latitude},${position.coords.longitude}`
    ubicacion.setAttribute('href', `/location/${loc}`)
}

ubicacion.addEventListener('click', () => {
    console.log(ubicacion.getAttribute('href'));
    if (!ubicacion.getAttribute('href')) alert('No has concedido permisos para acceder a tu ubicación, recarga la página y acepta los permisos')
})

window.onload = getLocation()
