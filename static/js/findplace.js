const boxSearch = document.getElementById('box-search')
const buttonSearch = document.getElementById('button-search')

buttonSearch.addEventListener('click', () => {
    const itemResults = Array.from(document.querySelectorAll('.item-result'))

    for(const item of itemResults) {
        if(item.textContent.toLowerCase().indexOf(boxSearch.value.toLowerCase()) == -1) {
            item.classList.replace('show-item', 'hide-item')
        } else item.classList.replace('hide-item', 'show-item')
    }
})