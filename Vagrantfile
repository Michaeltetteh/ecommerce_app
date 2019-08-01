# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
  echo "-------------------- updating package lists"
  apt-get update

  #install python3.7
  sudo apt-get install -y python3.7
  sudo apt install -y python3-pip
  sudo apt-get install -y python3-venv

  # gotta put this before the upgrade, b/c it reboots and then all commands are lost
  echo "-------------------- installing postgres"
  apt-get install postgresql

  # fix permissions
  echo "-------------------- fixing listen_addresses on postgresql.conf"
  sudo sed -i "s/#listen_address.*/listen_addresses '*'/" /etc/postgresql/10/main/postgresql.conf

  echo "-------------------- fixing postgres pg_hba.conf file"
  # replace the ipv4 host line with the above line
  # Accept all IPv4 connections - FOR DEVELOPMENT ONLY!!!
  sudo cat >> /etc/postgresql/10/main/pg_hba.conf <<EOF
    host    all         all         0.0.0.0/0             md5
    EOF

  echo "-------------------- creating postgres vagrant role with password vagrant"
  # Create Role and login
  sudo su postgres -c 'psql -c "CREATE ROLE vagrant SUPERUSER LOGIN PASSWORD 'vagrant'" '
  
  echo "-------------------- creating ecommerce database"
  # Create ecommerce database
  sudo su postgres -c "createdb -E UTF8 -T template0 --locale=en_US.utf8 -O vagrant ecommerce"
  
  echo "-------------------- upgrading packages to latest"
  apt-get upgrade -y

  sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
  sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2

  sudo update-alternatives --config python3
  #create ecommerce env
  # python3 -m venv ecommerce-venv

  # source ecommerce_venv/bin/activate

  # pip install -r requirements.txt

SCRIPT

Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-18.04"
  config.vm.hostname = "Ecommerce"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  config.vm.network "forwarded_port", guest: 5432, host: 15432, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder ".", "/home/vagrant/ecommerce_app"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    # vb.gui = true
  
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
  # config.vm.provision "shell", inline: $script
end
