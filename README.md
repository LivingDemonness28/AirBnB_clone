<h1>AirBnB clone - The console</h1>

<hr>

<h2>Concepts</h2>
<ul>
    <li><a href="https://intranet.alxswe.com/concepts/66" target="_blank">Python packages</a></li>
    <li><a href="https://intranet.alxswe.com/concepts/74" target="_blank">AirBnB clone</a></li>
</ul>

<hr>

![alt-text](https://raw.githubusercontent.com/Dikachis/AirBnB_clone/main/web_static/images/65f4a1dd9c51265f49d0.png)

<hr>

<h2>Background Context</h2>
<h3>Welcome to the AirBnB clone project!</h3>

<p>Before starting, please read the <strong>AirBnB</strong> concept page.</p>

<h3>First step: Write a command interpreter to manage your AirBnB objects.</h3>

<p>This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…</p>

<p>Each task is linked and will help you to:</p>
<ul>
    <li>put in a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
    <li>create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file</li>
    <li>create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>...) that inherit from <code>BaseModel</code></li>
    <li>create the first abstracted storage engine of the project: File storage.</li>
    <li>create all unittests to validate all our classes and storage engine</li>
</ul>

<hr>

<h2>What's a command interpreter?</h2>

<p>Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
    <li>Create a new object (ex: a new User or a new Place)</li>
    <li>Retrieve an object from a file, a database etc...</li>
    <li>Do operations on objects (count, compute stats, etc...)</li>
    <li>Update attributes of an object</li>
    <li>Destroy an object</li>
</ul>

<hr>

<h2>Resources</h2>
<p><strong>Read or watch:</strong></p>
<ul>
    <li><a href="https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A" target="_blank">cmd module</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg" target="_blank">cmd module in depth</a></li>
    <li><strong>packages</strong> concept page</li>
    <li><a href="https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ" target="_blank">uuid module</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA" target="_blank">datetime</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA" target="_blank">unittest module</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng" target="_blank">args/kwargs</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw" target="_blank">Python test cheatsheet</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ" target="_blank">cmd module wiki page</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA" target="_blank">python unittest</a></li>
</ul>

<hr>

<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/uV5eZkRZ_XEqYbgPd-0CWw" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>
<ul>
    <li>How to create a Python package</li>
    <li>How to create a command interpreter in Python using the <code>cmd</code> module</li>
    <li>What is Unit testing and how to implement it in a large project</li>
    <li>How to serialize and deserialize a Class</li>
    <li>How to write and read a JSON file</li>
    <li>How to manage <code>datetime</code></li>
    <li>What is an <code>UUID</code></li>
    <li>What is <code>*args</code> and how to use it</li>
    <li>What is <code>**kwargs</code> and how to use it</li>
    <li>How to handle named arguments in a function</li>
</ul>

<h3>Copyright - Plagiarism</h3>
<ul>    
    <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
    <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.</li>
    <li>You are not allowed to publish any content of this project.</li>
    <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>