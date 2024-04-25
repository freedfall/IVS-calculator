
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

document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', function() {
        this.blur();
    });
});

class Stack{
    constructor(){
        this.items = [];
    }
    push(element){
        this.items.push(element);
    }
    pop(){
        if (this.items.length === 0){
            return "Underflow";
        }
        
        let item = this.items.pop();
        let expr = `${item.type}[${item.base}, ${item.exponent}]`;

        let topItem = this.peek();
        if (topItem){
            if (topItem.state === 'base'){
                topItem.base += expr;
                isEnteringRootPower = false;
            } else{
                topItem.exponent += expr;
            }
        } else{
            calculationExpression += expr;
            isEnteringRootPower = false;
            isEnteringExponent = false;
            stackState = false;
        }
    }
    peek(){
        if (this.items.length === 0){
            return false;
        }
        return this.items[this.items.length - 1];
    }
    isEmpty(){
        return this.items.length === 0;
    }
}

/**
 * @class StackItem
 * @attribute state - base, exponent
 */
class StackItem {
    constructor(type, position){
        this.state = 'base';
        this.type = type;
        this.base = '';
        this.exponent = '';
        this.position = position;
    }
}

let log = '';
let root = '';
let stack = new Stack();
let exponent = '';
let rootPower = '';
let rootValue = '';
let expression = '';
let lastResult = '';
let baseExpression = '';
let expressionPower = '';
let calculationExpression = '';
let binaryMode = false;
let isEnteringExponent = false;
let isEnteringRootPower = false;
let stackState = false; // if we are in stack
const display = document.getElementById('display');
const originalFontSize = parseFloat(window.getComputedStyle(document.getElementById('display')).fontSize);
const maxLength = 8;

document.addEventListener('keydown', function (event) {
    const display = document.getElementById('display');
    const key = event.key;

    let allowedKeys = []
    console.log(key);
    // accept only the following keys
    if (binaryMode){
        allowedKeys = ['0', '1', '+', '-', '*', '/', '(', ')', '%', '!'];
    } else{
        allowedKeys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.', '(', ')', '%', '!', 'Enter'];
    }
    if (allowedKeys.includes(key)) {
        console.log('svyat govnoed');
        appendToDisplay(key);
    } else if (key === '=') {
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
        insertPower();
    } else if (stackState){
        handleStackExpression(value);
        handleView(value);
    } else if (value === 'rand'){
        generateRandomNumber();
    } else {
        if (binaryMode && ['0', '1', '+', '-', '*', '/', '(', ')', '%', '!'].includes(value) || !binaryMode){
            if (lastResult !== '' && ['+', '-', '*', '/', '%', '!'].includes(value) && expression === '') {
                expression += lastResult;
                calculationExpression += lastResult;
                handleView(value);
                handleCalculationExpression(value);
            }
            else{
                handleView(value);
                handleCalculationExpression(value);
            }
        } 
    }
    document.getElementById('display').innerHTML = expression;
}

function handleStackExpression(value){
    let state = stack.peek().state;
    console.log(state);
    if (state === 'base'){
        if (value === '√'){
            insertRoot();
        } else if (value === 'x^n'){
            insertPower();
        } else if (value === 'Enter' || value === '='){
            if (stack.peek().type === 'r'){
                handleView(')');
            }
            stack.peek().state = 'exponent';
            isEnteringRootPower = true;
            isEnteringExponent = true;
        } else{
            stack.peek().base += value;
        }
    } else if (state === 'exponent'){
        if (value === '√'){
            console.log(isEnteringRootPower);
            insertRoot();
        } else if (value === 'x^n'){
            insertPower();
        } else if (value === 'Enter' || value === '='){
            stack.pop();
        } else{
            stack.peek().exponent += value;
        }
    }
}

function get_position(){
    if (stackState){
        return stack.peek().position;
    } else {
        return expression.length;
    }
}

function handleView(value){
    if (expression.length >= maxLength) {
        const display = document.getElementById('display');
        const currentFontSize = parseFloat(window.getComputedStyle(display).fontSize);
        display.style.fontSize = (currentFontSize - 1.7) + 'px';
    }
    if (value === 'rand'){
        generateRandomNumber();
    }
    if (!isEnteringExponent && !isEnteringRootPower){
        if (value != 'Enter' && value != 'rand'){
            expression += value;
        }
    } else if (isEnteringRootPower){
        if (value != 'Enter' && value != 'rand'){
            rootPower = value;
            index = stack.peek().position;
            console.log(position);
            stack.peek().position = stack.peek().position + value.length;
            console.log(stack);
            expression = expression.slice(0, index) + rootPower + expression.slice(index);
        }
    } else if (isEnteringExponent){
        if (value != 'Enter' && value != 'rand'){
            exponent = `<sup class="root-power">${value}</sup>`;
            index = stack.peek().position + 1;
            stack.peek().position = stack.peek().position + value.lenght;
            expression = expression.slice(0, index) + exponent + expression.slice(index);
        }
    }
}

function handleCalculationExpression(value){
    if (!stackState && value !== 'Enter' && value !== 'rand'){
        calculationExpression += value;
    }
}

function generateRandomNumber(){
    if (binaryMode){
        value = ''
        for (let i = 0; i < 8; i++){
            value += Math.floor(Math.random() * 2);
        }
        handleView(value);
        handleCalculationExpression(value);
    } else{
        value = Math.floor(Math.random() * Math.floor(101));
        handleView(value);
        handleCalculationExpression(value);
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
    stackState = true;
    if (isEnteringRootPower){
        position = stack.peek().position;
    } else{
        position = expression.length;
    }
    item = new StackItem('r', position);
    stack.push(item);

    handleView('√(');
}

function insertPower(){
    stackState = true;
    if (isEnteringExponent){
        position = stack.peek().position + 1;
    } else {
        position = expression.length + 1;
    }
    item = new StackItem('p', position);
    stack.push(item);
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

function toggleLog() {
    const logElement = document.getElementById('log');
    if (logElement.style.display === 'none') {
        logElement.style.display = 'block';
        logElement.innerHTML = log;
    }
    else {
        logElement.style.display = 'none';
    }
}
function clearDisplay() {
    expression = '';
    calculationExpression = '';
    rootPower = '';
    rootValue = '';
    root = '';
    baseExpression = '';
    exponent = '';
    lastResult = ''
    isEnteringExponent = false;
    isEnteringRootPower = false;
    display.innerHTML = '';
    document.getElementById('output').value = '';
    applyAnimation(display);
    applyAnimation(output);
}

function handleLog(){
    //count the number of <br> tags in the log
    let count = (log.match(/<br>/g) || []).length;
    if (count > 3){
        //delete the first line
        let firstLine = log.split('<br>')[0];
        log = log.replace(firstLine + '<br>', '');
        document.getElementById('log').innerHTML = log;
    }
}

async function calculate() {
    if (!isEnteringRootPower && !isEnteringExponent) {
        try {
            let result = ''
            if (binaryMode){
                result = await eel.calculate(calculationExpression, binaryMode)();
                result = parseInt(result).toString(2);
            } else{
                result = await eel.calculate(calculationExpression, binaryMode)();
                console.log(calculationExpression);
            }
            document.getElementById('output').value = result;
            
            lastResult = result;
            handleLog();
            log += expression + '<br>';
            if (document.getElementById('log').style.display === 'block') {
                document.getElementById('log').innerHTML = log;
            }
            expression = ''; // Clear the expression after calculating
            calculationExpression = ''; // Clear the calculation expression after calculating
            
            applyAnimation(output); 
            const currentFontSize = parseFloat(window.getComputedStyle(document.getElementById('display')).fontSize);
            if (currentFontSize < originalFontSize) {
                // back to the original font size
                display.style.fontSize = originalFontSize + 'px';
            }

            isEnteringExponent = false;
            isEnteringRootPower = false;
        } catch (error) {
            console.log(error);
            document.getElementById('output').value = 'Error';
            applyAnimation(output);
        }
    }
    // else if (isEnteringRootPower) {
    //     isEnteringRootPower = false;
    //     rootValue = root.split('√')[1];
    //     rootPower = await eel.calculate(rootPower, binaryMode)();
    //     calculationExpression = calculationExpression.replace(`${root}`, `r[${rootPower}, ${rootValue}]`);

    //     rootPower = '';
    //     rootValue = '';
    //     root = '';
    // }
    // else if (isEnteringExponent) {
    //     calculationExpression = calculationExpression.replace(expressionPower, `p[${baseExpression}, ${exponent}]`);
    //     isEnteringExponent = false;
    //     exponent = '';
    //     expressionPower = '';
    //     baseExpression = '';
    // }
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
