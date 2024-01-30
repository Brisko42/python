# -*- encoding: utf-8 -*-
# stub: vagrant-scp 0.5.9 ruby lib

Gem::Specification.new do |s|
  s.name = "vagrant-scp".freeze
  s.version = "0.5.9"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Luca Invernizzi".freeze]
  s.date = "2021-11-08"
  s.description = "Copy files to a Vagrant VM via SCP.".freeze
  s.email = ["invernizzi.l@gmail.com".freeze]
  s.homepage = "https://github.com/invernizzi/vagrant-scp".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.3.26".freeze
  s.summary = "Copy files to a Vagrant VM via SCP.".freeze

  s.installed_by_version = "3.3.26" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_development_dependency(%q<bundler>.freeze, [">= 2.2.10"])
    s.add_development_dependency(%q<rake>.freeze, [">= 12.3.3"])
    s.add_runtime_dependency(%q<log4r>.freeze, ["~> 1.1"])
    s.add_runtime_dependency(%q<net-scp>.freeze, [">= 1.1"])
  else
    s.add_dependency(%q<bundler>.freeze, [">= 2.2.10"])
    s.add_dependency(%q<rake>.freeze, [">= 12.3.3"])
    s.add_dependency(%q<log4r>.freeze, ["~> 1.1"])
    s.add_dependency(%q<net-scp>.freeze, [">= 1.1"])
  end
end
