---
layout: page
title: About
permalink: /about/
---


<h1>AP Computer Science Principles</h1>

**Tarun Rayavarapu**

**Period 2**


<h2>About Me/Why I Took This Class:</h2>


My name is Tarun Rayavarapu and I am 15 years old. I took this class because both of my parents are software engineers, and very much enjoy their time in it. I also took this class because I want to learn coding and coding is the future of our world. I'm really interested in technology and thought this class would give me a good foundation for understanding it better. Also, I know that computer science is an important skill for many careers, so I thought it would be useful for my future. Lastly, I wanted to challenge myself with a more advanced class like this class to see if I could handle it.
![Alt text](https://i.insider.com/601441dd6dfbe10018e00c25?width=1136&format=jpeg)


<h2>What I Enjoy</h2>

<img src="https://i.etsystatic.com/6397925/r/il/b0f6c7/894698406/il_570xN.894698406_927u.jpg" alt="Image 1" width="150">

<img src="https://i.etsystatic.com/6397925/r/il/825ef9/886345972/il_570xN.886345972_m7nf.jpg" alt="Image 2" width="150">

<img src="https://www.pngkey.com/png/detail/403-4030326_japan-food-png-japanese-dinner-png.png" alt="Image 3" width="150">


<h2>My Background:</h2>

My family from both my Mom and my Dad side are from India, making me an Indian descendant. There are many flags I associate with, including:

var container = document.getElementById("grid_container");

var http_source = "https://upload.wikimedia.org/wikipedia/commons/";
var living_in_the_world = [
    {"flag": "a/a4/Flag_of_the_United_States.svg", "description": "US Flag"},
    {"flag": "4/41/Flag_of_India.svg", "description": "Indian Flag"},
    {"flag": "0/01/Flag_of_California.svg", "description": "California Flag"},
    {"flag": "6/6a/Flag_of_New_Jersey.svg", "description": "New Jersey Flag"},
];

for (const location of living_in_the_world) {
    var gridItem = document.createElement("div");
    gridItem.className = "grid-item";

    var img = document.createElement("img");
    img.src = http_source + location.flag;
    img.alt = location.description + " Flag";

    var description = document.createElement("p");
    description.textContent = location.description;

    gridItem.appendChild(img);
    gridItem.appendChild(description);

    container.appendChild(gridItem);
}

