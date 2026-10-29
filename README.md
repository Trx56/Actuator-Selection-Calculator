# Robotic Actuator Selection Calculator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Actuator Selection Calculator* is a Python-based Command Line Interface (CLI) tool that digitizes a hardware selection flowchart. Originally developed from an academic case study of commercial actuators, this tool evaluates user-inputted physics and power constraints to recommend optimal commercial motors and fluid drives for robotic applications.

---

## Key Features

* **Dynamic Decision Logic:** Evaluates variables like load capacity (e.g., >500kg triggers hydraulic recommendations) and motion speed requirements.
* **Commercial Hardware Mapping:** Recommends specific real-world actuators based on the inputs, including the Bosch Rexroth CDH1, Festo ADN, ODrive D6374, TowerPro MG996R, and Maxon DCX.
* **Battery Constraint Analysis:** Factors in mobile/battery-powered limitations to intelligently choose between high-speed BLDC motors and precise DC Servos.

---

##  Tech Stack & Libraries
* **Language:** Python
* **Interface:** Command Line Interface (CLI)

---

##  Code Architecture
```text
 Actuator-Selection-Calculator
 ┣  calculator.py       # Core logic gates and CLI prompt engine
 ┗  README.md           # Project documentation
