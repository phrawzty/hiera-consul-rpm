Name:       hiera-consul
Version:    0.0.6
Release:    1%{?dist}
Summary:    Consul backend for Hiera
License:    ASLv2
URL:        https://forge.puppetlabs.com/lynxman/hiera_consul
Group:      Development/Tools
Source0:    https://github.com/lynxman/%{name}/archive/v%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

%description
Consul backend for Hiera.

%prep
%setup -q

%install
mkdir -p %{buildroot}/%{_sysconfdir}/puppet/modules/hiera_consul/lib/hiera/backend
cp lib/hiera/backend/consul_backend.rb %{buildroot}/%{_sysconfdir}/puppet/modules/hiera_consul/lib/hiera/backend
mkdir -p %{buildroot}/%{_sysconfdir}/puppet/modules/hiera_consul/lib/puppet/parser/functions
cp lib/puppet/parser/functions/consul_info.rb %{buildroot}/%{_sysconfdir}/puppet/modules/hiera_consul/lib/puppet/parser/functions

%clean
rm -rf %{buildroot}

%files
%doc README.md
%defattr(-,root,root,-)
%dir %attr(755, root, root) %{_sysconfdir}/puppet/modules/hiera_consul
%attr(644, root, root) %{_sysconfdir}/puppet/modules/hiera_consul/lib/hiera/backend/consul_backend.rb
%attr(644, root, root) %{_sysconfdir}/puppet/modules/hiera_consul/lib/puppet/parser/functions/consul_info.rb

%changelog
* Wed Mar 18 2015 Dan Phrawzty <phrawzty@mozilla.com>
- init
