var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext('2d');
var blockX = canvas.width/10;
var blockY = canvas.width/10;
var blockPosX = 0; //Math.floor((Math.random()*300));
var blockPosY = 0;
var blockPosdX = 1;
var blockPosdY = 1;
var binSize = canvas.width/10;
var count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];


document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(e) {
    if(e.key == "Right" || e.key == "ArrowRight") {rightPressed = true;}
    else if(e.key == "left" || e.key == "ArrowLeft") {leftPressed = true;}
}
function keyUpHandler(e) {
    if(e.key == "Right" || e.key == "ArrowRight") {rightPressed = false;}
    else if(e.key == "left" || e.key == "ArrowLeft") {leftPressed = false;}
}
function drawBlock(x, y) {
    ctx.beginPath();
    ctx.rect(x, y, blockX, blockY);
    ctx.fillStyle = '#FF0000';
    ctx.fill();
    ctx.closePath();
}
function stackBlocks() {
    if(blockPosY + blockY > canvas.height) {
        blockPosY = 0;
        switch(blockPosX){
            case 0: 
                count[0] += 1;
                drawBlock(0, blockY)
                break; 
            case 32 : 
                count[1] += 1; 
                break; 
            case 64: 
                count[2] += 1; 
                break; 
            case 96 : 
                count[3] += 1; 
                break; 
            case 128 : 
                count[4] += 1; 
                break;
            case 160: 
                count[5] += 1; 
                break; 
            case 192 : 
                count[6] += 1; 
                break; 
            case 224: 
                count[7] += 1; 
                break; 
            case 256 : 
                count[8] += 1; 
                break; 
            case 288 : 
                count[9] += 1; 
                break;
        }
    } 
    else {blockPosY += blockPosdY;}
    console.log(count)
}
function moveBlock() {
    if(rightPressed && blockPosX < canvas.width - blockX) {blockPosX += binSize;}
    else if(leftPressed && blockPosX > 0) {blockPosX -= binSize;}
}
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBlock(blockPosX, blockPosY);
    stackBlocks();
    moveBlock();
    console.log(blockPosX)
    
}
var interval = setInterval(draw, 10);