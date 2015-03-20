# RPM spec for hiera-consul

This is an RPM spec for [hiera-consul](https://github.com/lynxman/hiera-consul/).

It installs the libraries into `/etc/puppet/modules/hiera_consul/` and the
README in `/usr/share/doc/hiera-consul-<version>`.

That's it.

# Build

To build the RPM (non-root user):

* Check out this repo. Nice, no?
* Install `rpmdevtools` and `mock`. 
    ```
    sudo yum install rpmdevtools mock
    ```

* Set up your rpmbuild directory tree.
    ```
    rpmdev-setuptree
    ```

* Link the spec file and sources.
    ```
    ln -s $HOME/hiera-consul-rpm/hiera-consul.spec rpmbuild/SPECS/
    ```

* Download remote source files.
    ```
    spectool -g -R rpmbuild/SPECS/hiera-consul.spec
    ```

* Build the RPM.
    ```
    rpmbuild -ba rpmbuild/SPECS/hiera-consul.spec
    ```
