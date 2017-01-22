Python service sample
=====================

```sh
# Clone repository
cd /opt
sudo git clone https://github.com/chmod644/pyservice

# Copy service file
cd pyservice
sudo cp ./sample/pyservice.service /etc/systemd/system/

# Make service enable
sudo systemctl enable pyservice

# Start service
sudo systemctl enable pyservice

# Check service
systemctl status pyservice

# Stop service
sudo systemctl stop service
```


