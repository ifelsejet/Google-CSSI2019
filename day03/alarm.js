let firstName = "Jet";

const sayHello = () => {
  let greeting = "Hello";
  firstName = "Jatnael";
  console.log(greeting + " " + firstName);
};

//anon function -> function w/o a name
//aka the messy way








/*
const sayHello = () => {
  console.log("Hello");
};
*/

//the messy way
/*
setTimeout(() => {
  console.log("Hello!");
}, 3000);
*/

//used to set an interval of when to do something
/*
setInterval(() => {
  console.log("Hello!");
}, 3000);
*/


//setTimeout(functioName, milliseconds);

//setTimeout(sayHello, 3000);

/*
const snoozeAlarm = (time) =>{
  return "The alarm for " + time + " has been changed to " + (time +1);
};
*/
