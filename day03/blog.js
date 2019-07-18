//querySelector can only get 1 item, or 0 if nothing is found.
const headerElement = document.querySelector("#header");

setInterval(() => {
  headerElement.style.color = "red";
}, 3000);


//span is just the text
const subHeaderElement = document.querySelector('#subheader span');

subHeaderElement.addEventListener('mouseover', () => {
  subHeaderElement.classList.add("blueText");
  //to remove --> .remove();
  //.toggle(); is  a thing too
  //subHeaderElement.innerHTML = 'Hello';
  //subHeaderElement.innerHTML = '<a href="www.google.com">Google</a>'';
});

/*
subHeaderElement.addEventListener('mouseleave', () => {
  subHeaderElement.style.color = 'black';
});
*/