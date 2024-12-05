const swapBtn1 = document.querySelector('#swap-btn1')
const swapBtn = document.querySelector('#swap-btn')
const htmlEl = document.getElementsByTagName('html')[0];
const icons = document.querySelector('#icons')

// Event listener on button

swapBtn.addEventListener('click', () => {
    // container.classList.add('dark')
    const rotation = parseInt(getComputedStyle(icons).getPropertyValue('--rotation'))
    icons.style.setProperty('--rotation', rotation - 180)

    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark')
    } else {
        document.documentElement.classList.remove('dark')
    }
    localStorage.theme = 'dark'
})
swapBtn1.addEventListener('click', () => {
    // container.classList.remove('dark')
    const rotation = parseInt(getComputedStyle(icons).getPropertyValue('--rotation'))
    icons.style.setProperty('--rotation', rotation - 180)

    localStorage.theme = 'light'
})
const toggleTheme = (theme) => {

    htmlEl.dataset.theme = theme;
}