console.log('hola');
const searchPlace = document.getElementById('searchPlace')

searchPlace.addEventListener('click', () => {
    const containerSearch = document.getElementById('containerSearch')
    containerSearch.classList.toggle('show-container-search')
})

const closeSearch = document.getElementById('closeContainerSearch')

closeSearch.addEventListener('click', () => {
    console.log('click');
    const containerSearch = document.getElementById('containerSearch')
    containerSearch.classList.toggle('show-container-search')
})