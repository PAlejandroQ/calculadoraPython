pipeline{
	agent{
		docker{
			image 'python:3.9.16-slim-bullseye'
		 }
	}
	triggers {
                pollSCM('* * * * *')
        }
	stages("Ejecucion"){
		steps{
			sh "python3 calculador.py 24 12
		}
	}
	stages("Tests"){
                steps{
                        sh "python3 -m unittest -v test_calculador.py"
                }
        }

}
