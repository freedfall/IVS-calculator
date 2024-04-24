
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
let binaryMode = false;
const display = document.getElementById('display');
const originalFontSize = parseFloat(window.getComputedStyle(document.getElementById('display')).fontSize);
const maxLength = 8;

document.addEventListener('keydown', function (event) {
    const display = document.getElementById('display');
    const key = event.key;

    let allowedKeys = []
    // accept only the following keys
    if (binaryMode){
        allowedKeys = ['0', '1', '+', '-', '*', '/', '(', ')', '%'];
    } else{
        allowedKeys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.', '(', ')', '%'];
    }
    if (allowedKeys.includes(key)) {
        appendToDisplay(key);
    } else if (key === 'Enter' || key === '=') {
        calculate();
        event.preventDefault();
    } else if (key === 'Backspace') {
        const currentFontSize = parseFloat(window.getComputedStyle(document.getElementById('display')).fontSize);
        if (currentFontSize < originalFontSize) {
            // back to the original font size
            display.style.fontSize = (currentFontSize + 1.7) + 'px';
        }
        expression = expression.slice(0, -1);
        calculationExpression = calculationExpression.slice(0, -1);
        display.innerHTML = expression;
    } else if (key === 'Escape') {
        clearDisplay();
        event.preventDefault();
    }
});

function appendToDisplay(value) {
    if (value === 'bin'){
        toggleBinaryMode();
    } else if (value === '√' && !binaryMode) {
        insertRoot();
    } else if (value === 'x^n' && !binaryMode) {
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
    } else if (isEnteringExponent) {
        updatePower(value);
    } else if (value === 'rand'){
        generateRandomNumber();
    } else {
        if (expression.length >= maxLength) {
            const display = document.getElementById('display');
            const currentFontSize = parseFloat(window.getComputedStyle(display).fontSize);
            display.style.fontSize = (currentFontSize - 1.7) + 'px';

        }
        if (binaryMode && ['0', '1', '+', '-', '*', '/', '(', ')', '%', '!'].includes(value) || !binaryMode){
            expression += value;
            calculationExpression += value;
        } 
    }
    document.getElementById('display').innerHTML = expression;
}

function generateRandomNumber(){
    if (binaryMode){
        value = ''
        for (let i = 0; i < 8; i++){
            value += Math.floor(Math.random() * 2);
        }
        expression += value;
        calculationExpression += value;
    } else{
        value = Math.floor(Math.random() * Math.floor(101));
        expression += value;
        calculationExpression += value;
    } 
}

function toggleBinaryMode(){
    binaryMode = !binaryMode;
    if (binaryMode){
        document.documentElement.setAttribute('keys-theme', 'binary');
    } else{
        document.documentElement.setAttribute('keys-theme', 'default');
    }
}

function convertExpressionToDecimal(){
    // Regular expression to find binary numbers adjacent to arithmetic operators or at the start/end of the string
    const binaryRegex = /(^|\s|[\+\-\*\/\(])([01]+)(\s|[\+\-\*\/\)]|$)/g;

    // Replace each binary number with its decimal equivalent
    calculationExpression = calculationExpression.replace(binaryRegex, (match, p1, p2, p3) => {
        const decimal = parseInt(p2, 2).toString(10); // Convert binary to decimal
        return p1 + decimal + p3; // Reattach the parts of the expression
    });
}

function insertRoot() {
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
    applyAnimation(display);
    applyAnimation(output);
}

async function calculate() {
    if (!isEnteringRootPower && !isEnteringExponent) {
        try {
            let result = ''
            if (binaryMode){
                result = await eel.calculate(calculationExpression, binaryMode)();
                result = parseInt(result).toString(2);
            }
            else{
                result = await eel.calculate(calculationExpression, binaryMode)();
            }
            document.getElementById('output').value = result;
            expression = ''; // Clear the expression after calculating
            calculationExpression = ''; // Clear the calculation expression after calculating
            applyAnimation(output); 
            const currentFontSize = parseFloat(window.getComputedStyle(document.getElementById('display')).fontSize);
            if (currentFontSize < originalFontSize) {
                // back to the original font size
                display.style.fontSize = originalFontSize + 'px';
            }
        } catch (error) {
            console.log(error);
            document.getElementById('output').value = 'Error';
            applyAnimation(output);
        }
    }
    else if (isEnteringRootPower) {
        isEnteringRootPower = false;
        rootValue = root.split('√')[1];
        rootPower = await eel.calculate(rootPower, binaryMode)();
        calculationExpression = calculationExpression.replace(`${root}`, `r[${rootPower}, ${rootValue}]`);

        rootPower = '';
        rootValue = '';
        root = '';
    }
    else if (isEnteringExponent) {
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
