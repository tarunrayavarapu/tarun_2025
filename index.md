---
layout: base
title: Student Home 
description: Home Page
hide: true
---



<h1>Tarun Rayavarapu



<table>
    <tr>
        <td width = "200"><img src="{{site.baseurl}}/images/download.jpeg" height="120" title="Pair" alt=""></td>
        <td><a href="/tarun_2025/about/">About Me</a></td>
        <td><a href="/tarun_2025/sports">Sports theme</a></td>
        <td><a href="/tarun_2025/games">Games</a></td>
        <td><a href="/tarun_2025/ideas">Ideas</a></td>
        <td><a href="{{site.baseurl}}/2024/09/19/newspaper_IPYNB_2_.html"> Jupyter Notebook Play </a></td>
    </tr>
</table>




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarun Rayavarapu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        header {
            text-align: center;
            margin-bottom: 30px;
        }
        nav a {
            margin: 0 10px;
            text-decoration: none;
            color: white;
            background-color: #007BFF;
            padding: 10px 15px;
            border-radius: 5px;
        }
        .link-container {
            margin: 10px 0;
            position: relative;
        }
        .dropdown {
            cursor: pointer;
            background-color: #007BFF;
            color: white;
            padding: 10px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .dropdown:hover {
            background-color: #0056b3;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            left: 0;
            top: 100%;
            background-color: white;
            color: black;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            width: 250px;
            z-index: 1;
        }
        .link-container:hover .dropdown-content {
            display: block;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>

<header>
    <h1>Tarun Rayavarapu</h1>
    <p>Class of 2027</p>
    <nav>
        <a href="/tarun_2025/blogs" class="btn">Blogs</a>
        <a href="/tarun_2025/about" class="btn">About</a>
        <a href="/tarun_2025/contact" class="btn">Contact</a>
    </nav>
</header>

<div class="link-container">
    <div class="dropdown">Variables and Assignments
        <div class="dropdown-content">
            <ul>
                <li>A variable is like a container that holds a value (such as a number or word) in a program.</li>
                <li>Variables have names so you can refer to them and use their values later.</li>
                <li>Assignment is the process of giving a variable a value using the = symbol (e.g., x = 5).</li>
                <li>Once assigned, you can use or change the value stored in the variable throughout your program.</li>
            </ul>
        </div>
    </div>
</div>

<div class="link-container">
    <div class="dropdown">Data Abstraction
        <div class="dropdown-content">
            <ul>
                <li>Explore how data abstraction helps in managing complexity.</li>
                <li>Abstracting details to focus on essential concepts.</li>
            </ul>
        </div>
    </div>
</div>

<div class="link-container">
    <div class="dropdown">Mathematical Expressions
        <div class="dropdown-content">
            <ul>
                <li>Basic Operations: Mathematical expressions in coding use operators like + (addition), - (subtraction), * (multiplication), and / (division).</li>
                <li>Order of Operations: Just like math, coding follows rules for order of operations (PEMDAS: parentheses, exponents, multiplication/division, addition/subtraction).</li>
                <li>Variables in Expressions: You can use variables to store numbers and include them in expressions (e.g., x + y).</li>
                <li>Combining Expressions: You can combine multiple expressions to perform more complex calculations (e.g., (a + b) * c).</li>
            </ul>
        </div>
    </div>
</div>

<div class="link-container">
    <div class="dropdown">Strings
        <div class="dropdown-content">
            <ul>
                <li>A string is a sequence of characters, like words or sentences, enclosed in quotes (e.g., "Hello").</li>
                <li>Manipulation: You can combine (concatenate) strings or break them into parts using various functions.</li>
                <li>Indexing: Strings are like lists of characters, where each character has a position (index) starting from 0.</li>
                <li>Common Operations: You can search for characters, change parts of a string, and check its length easily using built-in functions.</li>
            </ul>
        </div>
    </div>
</div>

<div class="link-container">
    <div class="dropdown">Boolean Expressions
        <div class="dropdown-content">
            <ul>
                <li>True/False Values: Boolean expressions evaluate to either true or false.</li>
                <li>Comparison Operators: Use operators like ==, !=, >, <, >=, and <= to compare values.</li>
                <li>Logical Operators: Combine expressions using AND (&&), OR (||), and NOT (!).</li>
                <li>Control Flow: Boolean expressions are often used in if statements to control the flow of a program based on conditions.</li>
            </ul>
        </div>
    </div>
</div>

<div class="link-container">
    <div class="dropdown">Conditionals
        <div class="dropdown-content">
            <ul>
                <li>If Statements: Checks if a condition is true, then runs a block of code.</li>
                <li>Else Statements: Runs a block of code if the previous "if" condition is false.</li>
                <li>Else If: Allows checking multiple conditions after an initial "if" statement.</li>
                <li>Nested Conditionals: Conditionals inside other conditionals to check more complex logic.</li>
            </ul>
        </div>
    </div>
</div>

<div class="link-container">
    <div class="dropdown">Nested Conditionals
        <div class="dropdown-content">
            <ul>
                <li>A nested conditional is an if-else statement inside another if-else statement.</li>
                <li>They help in checking multiple conditions, one after the other.</li>
                <li>The inner condition is only checked if the outer condition is true.</li>
                <li>Nested conditionals can make decisions more complex, so it's important to keep them clear and simple.</li>
            </ul>
        </div>
    </div>
</div>

<div class="link-container">
    <div class="dropdown">Iteration
        <div class="dropdown-content">
            <ul>
                <li>Repeats actions: Iteration allows a set of actions or instructions to be repeated multiple times.</li>
                <li>Uses loops: Common loops like for, while, and do-while help control how many times the code runs.</li>
                <li>Works with collections: Iteration is often used to go through items in a list, array, or other data structures.</li>
                <li>Saves time: Instead of writing repetitive code, iteration automates repeated tasks efficiently.</li>
            </ul>
        </div>
    </div>
</div>

<div class="link-container">
    <div class="dropdown">Lists
        <div class="dropdown-content">
            <ul>
                <li>Maintains Order: Lists keep elements in the order they are added, making it easy to access them by their position.</li>
                <li>Flexible Size: You can change the size of a list at any time, adding or removing elements as needed.</li>
                <li>Mixed Data Types: Lists can hold multiple types of data together, like strings, numbers, and other lists.</li>
                <li>Easy Manipulation: Lists offer simple methods to manipulate data, such as adding, removing, or sorting elements.</li>
            </ul>
        </div>
    </div>
</div>

</body>
</html>


 


