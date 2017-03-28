## Instrucciones para correr script

Esta es una guía para correr el script **send_answers.py**     

**1.-** Clonar repo en tu máquina local  
**2.-** Ejecutar `systemctl status elasticsearch`  
En caso de estar abajo el servicio, se deberá ejecutar `systemctl start elasticsearch`  
**3.-** Ejecutar el siguiente comando: `python ./send_answers.py`  
**4.-** Comprobar en la url `http://localhost:9200/beeva/mary/1?pretty`
