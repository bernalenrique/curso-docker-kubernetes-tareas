# Proyecto Final

## Parte 1: Setup del Ambiente

### microk8s instalado con addons habilitados

![status](punto1/proyecto_p1-01.png)

### Proyecto v2.0 funcionando en el cluster

![status](punto1/proyecto_p1-02.png)

### Ingress resolviendo el frontend

**frontend Angular**

![inicio](punto1/proyecto_p1-03_a.png)

**JSON con el saludo**

![inicio](punto1/proyecto_p1-03_b.png)

**lista de usuarios**

![inicio](punto1/proyecto_p1-03_c.png)

**"status"**

![inicio](punto1/proyecto_p1-03_d.png)

### Identidad del ambiente validada

![hostname](punto1/proyecto_p1-04.png)

## Parte 2: Iteración v2.1 - Modificar Backend

### Código del endpoint agregado

![endpoint](punto2/proyecto_p2-01.png)

### docker images

![images](punto2/proyecto_p2-02_a.png)

### Link a imagen en Docker Hub
https://hub.docker.com/repository/docker/bernalconde/springboot-api/tags

![dockerhub](punto2/proyecto_p2-02_b.png)

### kubectl rollout status durante la actualización

![roullout](punto2/proyecto_p2-4_a.png)

![roullout](punto2/proyecto_p2-4_a.png)

**Nota:** Se presento un error durante el rollout debido a una mala configuracion en la adicion de un nuevo endpoint, se adiciono el nuevo endpoint a la misma ruta. Una vez corregido el error se procedio a repetir el ciclo de construcion y despliegue.

### kubectl get pods

![pods](punto2/proyecto_p2-5.png)

### output de curl http://192.168.1.240/api/info

![curl](punto2/proyecto_p2-6.png)

