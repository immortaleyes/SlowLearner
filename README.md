<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Academic Dashboard README</title>
</head>
<body>
<h1>Academic Dashboard with Faculty & Subject Details</h1>

<p>This project is an interactive academic dashboard created using Python with the Dash and Plotly libraries. It visualizes various metrics related to academic performance, attendance, and engagement levels for different coordinators, subjects, and faculty members. This dashboard is designed to help academic coordinators monitor and manage students' progress, especially focusing on slow learners.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#features">Features</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#screenshots">Screenshots</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="features">Features</h2>
<ul>
  <li><strong>Executive Overview</strong>: Provides a high-level view of total students and slow learners under each coordinator.</li>
  <li><strong>Department Insights</strong>: Visualizes the distribution of slow learners across different departments.</li>
  <li><strong>Faculty Impact Analysis</strong>: Analyzes engagement metrics like attendance, quiz completion, and assignment completion for each faculty member, segmented by selected coordinators and subjects.</li>
  <li><strong>Interactive Filtering</strong>: Allows filtering by coordinator and subject to drill down on specific data.</li>
</ul>

<h2 id="project-structure">Project Structure</h2>
<pre><code>
academic_dashboard_app.py  # Main code for running the dashboard
README.md                  # Project documentation
requirements.txt           # List of required packages
</code></pre>

<h2 id="installation">Installation</h2>
<h3>Prerequisites</h3>
<ul>
  <li>Python 3.7 or higher</li>
  <li><a href="https://pip.pypa.io/en/stable/">Pip</a></li>
</ul>

<h3>Steps</h3>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/immortaleyes/academic-dashboard.git
cd academic-dashboard
</code></pre>
  </li>
  <li>Install the required Python packages:
    <pre><code>pip install -r requirements.txt</code></pre>
    Alternatively, you can install the dependencies manually:
    <pre><code>pip install dash plotly pandas</code></pre>
  </li>
</ol>

<h2 id="usage">Usage</h2>
<p>To start the dashboard, run:</p>
<pre><code>python academic_dashboard_app.py</code></pre>
<p>After running the above command, open your browser and go to:</p>
<pre><code>http://127.0.0.1:8050</code></pre>

<h3>Interface Overview</h3>
<ul>
  <li><strong>Executive Overview Tab</strong>: Displays bar charts for total students and slow learners under each coordinator.</li>
  <li><strong>Department Insights Tab</strong>: Provides insights on slow learner distribution by department.</li>
  <li><strong>Faculty Impact Tab</strong>: Choose a coordinator and subject to view faculty performance metrics, slow learner data, and engagement metrics (attendance, quiz completion, and assignments).</li>
</ul>

<h2 id="screenshots">Screenshots</h2>
<p>Include a few screenshots of your dashboard here.</p>
<ul>
  <li><strong>Executive Overview</strong></li>
  <li><strong>Department Insights</strong></li>
  <li><strong>Faculty Impact Analysis</strong></li>
</ul>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
