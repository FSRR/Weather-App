const celsius = document.getElementById('celsius')
const fahrenheit = document.getElementById('fahrenheit')

celsius.addEventListener('click', () => {
    const mainGrade = document.getElementById('main-grade')
    if(mainGrade.children[0].textContent == '°F') {
        const secondaryGrades = Array.from(document.querySelectorAll('.secondary-grades'))
        
        const toCelsius = (mainGrade.dataset.scale - 32) * 5/9
        mainGrade.innerHTML = toCelsius.toPrecision(2) + "<span>°C</span>"
        mainGrade.setAttribute('data-scale', toCelsius.toPrecision(2))
    
        for(const item of secondaryGrades) {
            const itemToCelsius = (item.dataset.scale - 32) * 5/9
            item.textContent = itemToCelsius.toPrecision(2) + "°C"
            item.setAttribute('data-scale', itemToCelsius.toPrecision(2))
        }

        fahrenheit.classList.toggle('button-selected')
        celsius.classList.toggle('button-selected')
    }
})

fahrenheit.addEventListener('click', () => {
    const mainGrade = document.getElementById('main-grade')
    if(mainGrade.children[0].textContent == "°C") {
        const secondaryGrades = Array.from(document.querySelectorAll('.secondary-grades'))
        
        const toFahrenheit = (mainGrade.dataset.scale * 9/5) + 32
        mainGrade.innerHTML = toFahrenheit.toPrecision(2) + "<span>°F</span>"
        mainGrade.setAttribute('data-scale', toFahrenheit.toPrecision(2))
    
        for(const item of secondaryGrades) {
            const itemToFahrenheit = (item.dataset.scale * 9/5) + 32
            item.textContent = itemToFahrenheit.toPrecision(2) + "°F"
            item.setAttribute('data-scale', itemToFahrenheit.toPrecision(2))
        }

        celsius.classList.toggle('button-selected')
        fahrenheit.classList.toggle('button-selected')
    }
})