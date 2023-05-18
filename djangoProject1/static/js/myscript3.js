console.log('jiby')
let P1 = prompt("enter your name, you will be blue");
let P1Col = rgb("86 151 255");

let P2 = prompt("enter your name, you will be red");
let P2Col = rgb("237, 45, 73")

let game_on=true;
let table= $('table tr');

function reportWin(rowNum, colNum){
console.log("You won starting this row");
console.log(rowNum);
console.log(colNum);
}

$('button').click(function(){
$(this).text("I was clicked on")
$(this).toggleClass("turnred")
})


$('input').eq(0).keypress(function(){
if (event.which ===13)
{
$('h1').toggleClass("turnred")
console.log("Oho Ive changed the color too")
}
}
)