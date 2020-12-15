const ubicacion = document.getElementById('location')
let loc

function getLocation() {
    if (navigator.geolocation) {
        console.log(navigator);
        navigator.geolocation.getCurrentPosition(showPosition)
        console.log(navigator);
    } else {
        alert('No es compatible con tu navegador')
    }
}


function showPosition(position) {
    loc = `${position.coords.latitude},${position.coords.longitude}`
    ubicacion.href = `/location/${loc}`
    console.log(loc);
    return loc
}

// ubicacion.addEventListener('click', () => {
//     console.log(ubicacion.href);
//     if (ubicacion.href === '') alert('Tu ubicación está bloqueado, para acceder a tu ubicación haz click en el icono de ubicación de la barra de direcciones del navegador y actualiza la página')
//     // getLocation()
//     console.log(loc);
//     // if(loc) {
//     //     ubicacion.href = `/location/${loc}`
//     // } else console.log('Click otra vez');
// })

window.onload = getLocation()
