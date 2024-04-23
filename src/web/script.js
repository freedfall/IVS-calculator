
// Change the theme of the calculator
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
let baseExpression = '';
let expressionPower = '';
let exponent = '';
let isEnteringExponent = false;
let isEnteringRootPower = false;
let calculationExpression = '';
const display = document.getElementById('display');
const cursor = document.createElement('span');
cursor.className = 'blinking-cursor';

document.addEventListener('keydown', function(event) {
    const display = document.getElementById('display');
    const key = event.key;

    // Разрешенный список символов для ввода
    const allowedKeys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.', '(', ')', '%'];
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



const originalFontSize = parseFloat(window.getComputedStyle(document.getElementById('display')).fontSize);

function appendToDisplay(value) {    
    if (value === '√') {
        insertRoot();
        cursor.remove();
    } else if (value === 'x^n'){
        let lastNumberRegex = /[\d\.]+(?:[eE][+-]?\d+)?$/;
        let match = expression.match(lastNumberRegex);
        if (match) {
            // save last number or expression as exponent base
            baseExpression = match[0];
            expressionPower = baseExpression;
            exponent = '';
            isEnteringExponent = true;
        }
    } else if (isEnteringRootPower) {
        updateRootPower(value);
    } 
    else if (isEnteringExponent){
        updatePower(value);
    }
    else {
        expression += value;
        calculationExpression += value;
    }
    document.getElementById('display').innerHTML = expression;
    display.appendChild(cursor);
}

function insertRoot(){
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
}

function updateRootPower(value) {
    cursor.remove();
    rootPower += value;
    let updatedRoot = `<sup class='root-power'>${rootPower}</sup>${rootValue}`;
    expression = expression.replace(root, updatedRoot);
    calculationExpression = calculationExpression.replace(root, updatedRoot);
    root = updatedRoot;
}

function updatePower(value) {
    exponent += value;
    let updatedExpression = `${baseExpression}<sup class='root-power'>${exponent}</sup>`;
    expression = expression.replace(expressionPower, updatedExpression);
    calculationExpression = calculationExpression.replace(expressionPower, updatedExpression);
    expressionPower = updatedExpression;
}

function updatePower(value) {
    exponent += value;
    let updatedExpression = `${baseExpression}<sup class='root-power'>${exponent}</sup>`;
    expression = expression.replace(expressionPower, updatedExpression);
    calculationExpression = calculationExpression.replace(expressionPower, updatedExpression);
    expressionPower = updatedExpression;
}

function updatePower(value) {
    exponent += value;
    let updatedExpression = `${baseExpression}<sup class='root-power'>${exponent}</sup>`;
    expression = expression.replace(expressionPower, updatedExpression);
    calculationExpression = calculationExpression.replace(expressionPower, updatedExpression);
    expressionPower = updatedExpression;
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Backspace') {
        // if the font size is smaller than the original size
        const currentFontSize = parseFloat(window.getComputedStyle(document.getElementById('display')).fontSize);
        if (currentFontSize < originalFontSize) {
            // back to the original font size
            display.style.fontSize = (currentFontSize + 1.5) + 'px';
        }
    }
});

function clearDisplay() {
    expression = '';
    calculationExpression = '';
    rootPower = '';
    rootValue = '';
    root = '';
    baseExpression = '';
    exponent = '';
    isEnteringExponent = false;
    isEnteringRootPower = false;
    display.innerHTML = '';
    document.getElementById('output').value = '';
    display.appendChild(cursor);
    applyAnimation(display);
    applyAnimation(output);
}



async function calculate() {
    if (!isEnteringRootPower && !isEnteringExponent){
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
    else if (isEnteringRootPower){
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
    else if (isEnteringExponent){
        cursor.remove();
        display.appendChild(cursor);
        calculationExpression = calculationExpression.replace(expressionPower, `p[${baseExpression}, ${exponent}]`);
        isEnteringExponent = false;
        exponent = '';
        expressionPower = '';
        baseExpression = '';
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
