# Prepare config for pip (Ubuntu)

Before publishing, you need to create file .pypirc like this:

    [distutils]
    index-servers=
        pypi
        private_pypi
    
    [pypi]
    repository: https://upload.pypi.org/legacy/ 
    username: <username_pypi>
    password: <password_pypi>
    
    [private_pypi]
    repository: <private-pypi-registry>
    username: <username_private_pipy_registry>
    password: <password_private_pipy_registry>
    
You must to set this file into home directory. 

# Publish package to private_pypi pypi server

Before publish, set differences into CHANGELOG.md, setup.py version. After that, you need to create new release into master branch on 
github. Now, you need update package:

    python setup.py bdist_wheel upload -r private_pypi
    
This command push your image to pypi-package-registry

# Publish image into docker registry (for local development and testing)

From the root directory build the image

    docker-compose -f .deploy/docker-compose.local.yml build
    
After that, you must find the line with next text (last lines):

    Successfully built <image-id>
    Successfully tagged <image-name>:latest
    
Now, you must set tag for image:

    docker tag <image-id> <private-docker-registry>/<project>-<version>-<service-name>:<the-same-version-setup.py>
    
Please, add insecure-registry parameters to `/etc/docker/daemon.json`:

    {
        "insecure-registries" : [ "<private-docker-registry>" ]
    }
    
And restart docker:

    sudo service docker restart

Now, login in docker registry with your login and password:

    docker login <private-docker-registry> -u="<username>" -p="<password>"
    
Push the image:

    docker push <private-docker-registry>/<project>-<version>-<service-name>:<the-same-version-setup.py>
    
After that, you need remove image:

    docker rmi <image-id> --force

You can see images:

    http://<private-docker-registry>/v2/_catalog
 
Or concrete versions:

    http://<private-docker-registry>/v2/<image-name>/tags/list
    

    
