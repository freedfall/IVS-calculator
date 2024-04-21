document.addEventListener('DOMContentLoaded', () => {
    const checkbox = document.getElementById('checkbox');
    const isDarkMode = checkbox.checked || localStorage.getItem('theme') === 'dark';
    document.documentElement.setAttribute('data-theme', isDarkMode ? 'dark' : 'light');
    checkbox.checked = isDarkMode;
  });
  
document.getElementById('checkbox').addEventListener('change', function() {
    if (this.checked) {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.setAttribute('data-theme', 'light');
      localStorage.setItem('theme', 'light');
    }
});

document.addEventListener('keydown', function(event) {
    const display = document.getElementById('display');
    const key = event.key;

    // Разрешенный список символов для ввода
    const allowedKeys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.'];
    if (allowedKeys.includes(key)) {
        appendToDisplay(key);
    } else if (key === 'Enter' || key === '=') {
        calculate();
        event.preventDefault();
    } else if (key === 'Backspace') {
        expression = expression.slice(0, -1);
        display.value = expression;
    } else if (key === 'Escape') {
        clearDisplay();
    }
});

let expression = '';

function appendToDisplay(value) {
    expression += value;
    document.getElementById('display').value = expression;
}

function clearDisplay() {
    expression = '';
    document.getElementById('display').value = '';
    document.getElementById('output').value = '';
    applyAnimation(display);
    applyAnimation(output);
}

async function calculate() {

    try {
        let result = await eel.calculate(expression)();
        document.getElementById('output').value = result
        expression = result.toString();
        applyAnimation(output);
    } catch (error) {
        console.log(error)
        document.getElementById('output').value = 'Error';
        applyAnimation(output);
    }
}

function applyAnimation(element) {
    element.classList.remove('input-animate', 'output-animate');
    void element.offsetWidth; // Trigger reflow to restart animation
    if (element.id === 'display') {
        element.classList.add('input-animate');
    } else if (element.id === 'output') {
        element.classList.add('output-animate');
    }
}
