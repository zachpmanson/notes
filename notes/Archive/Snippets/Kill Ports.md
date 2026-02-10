A bash function to kill all processes running on a port.

```bash
function kport() {
    echo Killing the following processes:
    lsof -i -P -n |  grep ":$1" | tr -s ' ' | cut -d " " -f 1,2,9
    kill $(lsof -i -P -n |  grep ":$1" | tr -s ' ' | cut -d " " -f 2)   
    echo "All processes sent kill signal"
}
```