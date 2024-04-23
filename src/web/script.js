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

let expression = '';
let rootPower = '';
let rootValue = '';
let root = '';
let isEnteringRootPower = false;
let calculationExpression = '';
const display = document.getElementById('display');
const cursor = document.createElement('span');
cursor.className = 'blinking-cursor';

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
        calculationExpression = calculationExpression.slice(0, -1);
        display.innerHTML = expression;
    } else if (key === 'Escape') {
        clearDisplay();
    }
});



function appendToDisplay(value) {    
    if (value === '√') {
        // find last number in expression
        let lastNumberRegex = /[\d\.]+(?:[eE][+-]?\d+)?$/;
        let match = expression.match(lastNumberRegex);
        if (match) {
            matchCalc = calculationExpression.match(lastNumberRegex);
            let lastNumberIndex = match.index;
            let lastNumberIndexCalc = matchCalc.index;
            let lastNumber = match[0];
            // input root symbol
            expression = expression.slice(0, lastNumberIndex) + `√${lastNumber}` + expression.slice(lastNumberIndex + lastNumber.length);
            calculationExpression = calculationExpression.slice(0, lastNumberIndexCalc) + `√${lastNumber}` + calculationExpression.slice(lastNumberIndexCalc + lastNumber.length);
            root = `√${lastNumber}`;
            rootValue = root;
        } else {
            expression = `√()${expression}`;
            calculationExpression = `√()${expression}`;
            root = `√()`;
            rootValue = root;
        }
        isEnteringRootPower = true;
        rootPower = '';
        cursor.remove();
    } else if (isEnteringRootPower) {
        cursor.remove();
        rootPower += value;
        let updatedRoot = `<sup class='root-power'>${rootPower}</sup>${rootValue}`;
        expression = expression.replace(root, updatedRoot);
        calculationExpression = calculationExpression.replace(root, updatedRoot);
        root = updatedRoot;
    } else {
        expression += value;
        calculationExpression += value;
    }
    document.getElementById('display').innerHTML = expression;
    display.appendChild(cursor);
}

function clearDisplay() {
    expression = '';
    calculationExpression = '';
    rootPower = '';
    rootValue = '';
    root = '';
    isEnteringRootPower = false;
    display.innerHTML = '';
    document.getElementById('output').value = '';
    display.appendChild(cursor);
    applyAnimation(display);
    applyAnimation(output);
}

async function calculate() {
    if (!isEnteringRootPower){
        try {
            let result = await eel.calculate(calculationExpression)();
            document.getElementById('output').value = result
            expression = result.toString();
            calculationExpression = result.toString();
            applyAnimation(output);
        } catch (error) {
            console.log(error)
            document.getElementById('output').value = 'Error';
            applyAnimation(output);
        }
    }
    else {
        cursor.remove();
        display.appendChild(cursor);
        isEnteringRootPower = false;
        rootValue = root.split('√')[1];
        rootPower = await eel.calculate(rootPower)();
        calculationExpression = calculationExpression.replace(`${root}`, `r[${rootPower}, ${rootValue}]`);

        rootPower = '';
        rootValue = '';
        root = '';
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
