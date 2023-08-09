pipeline {
  agent {
    docker {
      image 'gradle:6-jdk11'
    }

  }
  stages {
    stage('Parallel execution') {
      parallel {
        stage('error') {
          steps {
            sh 'echo "hello world"'
          }
        }

        stage('build app') {
          agent {
            docker {
              image 'gradle:6-jdk11'
            }

          }
          steps {
            sh 'ci/build-app.sh'
          }
        }

      }
    }

  }
}