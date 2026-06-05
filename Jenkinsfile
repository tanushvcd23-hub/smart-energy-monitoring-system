pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\TANUSH\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\TANUSH\\AppData\\Local\\Python\\bin\\python.exe" test_energy.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t smart-energy-monitoring-system .'
            }
        }
    }
}
