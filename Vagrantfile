# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ansible.box"

  config.vm.provision "file", source: "roles", destination: "/etc/ansible/roles"
  config.vm.provision "file", source: "ansible_rsa", destination: "/etc/ansible/ansible_rsa"
  config.vm.provision "file", source: "ansible.cfg", destination: "/etc/ansible/ansible.cfg"
  config.vm.provision "file", source: "common.yml", destination: "/etc/ansible/common.yml"

  config.vm.define "gearman-proxy" do |gearman_proxy|
    gearman_proxy.vm.network "private_network", ip: "192.168.0.152", virtualbox__intnet: true
    gearman_proxy.vm.network "forwarded_port", guest: 22, host: 49152
    gearman_proxy.vm.network "forwarded_port", guest: 80, host: 80
    gearman_proxy.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-proxy"]' | tee /etc/ansible/facts.d/roles.fact
       ansible-playbook --inventory "192.168.0.152," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "gearman-server" do |gearman_server|
    gearman_server.vm.network "private_network", ip: "192.168.0.153", virtualbox__intnet: true
    gearman_server.vm.network "forwarded_port", guest: 22, host: 49153
    gearman_server.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-server"]' | tee /etc/ansible/facts.d/roles.fact
       ansible-playbook --inventory "192.168.0.153," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "gearman-worker" do |gearman_worker|
    gearman_worker.vm.network "private_network", ip: "192.168.0.154", virtualbox__intnet: true
    gearman_worker.vm.network "forwarded_port", guest: 22, host: 49154
    gearman_worker.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-worker", "gearman-ansible"]' | tee /etc/ansible/facts.d/roles.fact
       ansible-playbook --inventory "192.168.0.154," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "gearman-client", autostart: false do |debian|
    debian.vm.box = "gearman.box"
    debian.vm.network "private_network", ip: "192.168.0.155", virtualbox__intnet: true
    debian.vm.network "forwarded_port", guest: 22, host: 49155
    debian.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
       gearman -h 192.168.0.152 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
    SHELL
  end

  config.vm.define "galaxy", autostart: false do |init|
    init.vm.synced_folder ".", "/vagrant"
    init.vm.provision "shell", inline: <<-SHELL
      mkdir -p /vagrant/roles
      cd /vagrant/roles
      ansible-galaxy init gearman-server
    SHELL
  end

end
