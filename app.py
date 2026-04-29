from flask import Flask

app = Flask(__name__)

@app.route('/')
def portfolio():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Yuvadharshini | Portfolio</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
        }

        .container {
            width: 80%;
            margin: auto;
            padding: 20px;
        }

        h1 {
            color: #38bdf8;
            margin-bottom: 5px;
        }

        h2 {
            border-bottom: 2px solid #38bdf8;
            padding-bottom: 5px;
            margin-top: 30px;
        }

        p, li {
            line-height: 1.6;
        }

        .header {
            text-align: center;
            margin-bottom: 20px;
        }

        .contact {
            font-size: 14px;
            color: #94a3b8;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li::before {
            content: "➤ ";
            color: #38bdf8;
        }

        .project {
            margin-bottom: 15px;
        }

        a {
            color: #38bdf8;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .box {
            background: #1e293b;
            padding: 15px;
            border-radius: 10px;
            margin-top: 15px;
        }
    </style>
</head>
<body>

<div class="container">

    <div class="header">
        <h1>Yuvadharshini M</h1>
        <div class="contact">
            📧 yuvadharshinim05@gmail.com | 📞 9345844828 <br>
            🔗 LinkedIn | GitHub
        </div>
    </div>

    <div class="box">
        <h2>Career Objective</h2>
        <p>
            Passionate Information Technology student seeking opportunities to apply skills in programming,
            web development, and cybersecurity while continuously learning in a challenging technical environment.
        </p>
    </div>

    <div class="box">
        <h2>Education</h2>
        <ul>
            <li>Kongu Engineering College – B.Tech IT (CGPA: 8.13)</li>
            <li>HSC – 79.9%</li>
            <li>SSLC – 85%</li>
        </ul>
    </div>

    <div class="box">
        <h2>Technical Skills</h2>
        <ul>
            <li>Languages: C, C++, Java</li>
            <li>Web: HTML, CSS, React.js</li>
            <li>Database: OracleDB</li>
            <li>Tools: Git, GitHub, VS Code</li>
        </ul>
    </div>

    <div class="box">
        <h2>Projects</h2>

        <div class="project">
            <strong>SmartDNS</strong><br>
            AI-powered DNS filtering system for detecting malicious domains.<br>
            Tech: Python, ML, Unbound DNS
        </div>

        <div class="project">
            <strong>Craft Connect</strong><br>
            MERN platform for artisans and customers.<br>
            Tech: MongoDB, Express, React, Node
        </div>

        <div class="project">
            <strong>CyberNova</strong><br>
            Autonomous cyber defense system with SIEM features.<br>
            Tech: Python, LLM, SIEM
        </div>

    </div>

    <div class="box">
        <h2>Achievements</h2>
        <ul>
            <li>2nd Prize – Ideathon (CyberNova)</li>
            <li>3rd Prize – Ransomware Detection Project</li>
        </ul>
    </div>

    <div class="box">
        <h2>Soft Skills</h2>
        <ul>
            <li>Teamwork</li>
            <li>Adaptability</li>
            <li>Critical Thinking</li>
            <li>Problem Solving</li>
        </ul>
    </div>

</div>

</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
