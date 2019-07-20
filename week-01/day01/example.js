const headerElement = document.querySelector("#paragraph");
let counter = 0;

/*
setTimeout(() => {
  headerElement.style.color = 'blue';
}, 2000);
*/


let changeRandom = () => {
counter = (counter * (Math.random() * 100));


if(counter % 2 === 0){
  headerElement.style.color = 'green';
}
else {
  headerElement.style.color = 'blue';

}
};

setInterval(changeRandom,1000);
