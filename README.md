# Layerworx Linux
Layerworx Linux is an effort to create a unified container format, container host and virtualization host using a single code base. The reason for this effort is to close the disparity between running many different operating systems to accomplish a common goal. It is frequently accepted as commonplace that both container based applications and virtual machines co-exist in the same environment within our datacenters. However, we find ourselves increasingly learning multiple distributions of Linux and maintaing several different package versions of the same packages throughout our environment to accomplish our goals. This is meant to be a solution to that. A single distribution that can be ran inside of your containers, a single operating system to be a host to your containers and a virtualization hypervisor to run your container hosts.

## How this is built:
This project's skeleton is built using [Linux From Scratch](http://linuxfromscratch.org) as it's base. It's difficult to call this a fork, because the end product will not be a variant of Linux From Scratch, but a new product entirely. But, because of it's roots in LFS, this project will recognize LFS as the base component for our builds until a time that it may be replaced, which is unlikely.

## How to Contribute:
Fork and send pull requests. I'm accepting ONLY patches to our existing spec files at this time and no new spec files currently until we modernize the existing package library to current standards.

## Project Links
### Project Wiki
The official project wiki for Layerworx Linux can be found at GitHub currently under the [official repository](https://github.com/layerworx/linux/wiki). The wiki is sparse currently, but, will eventually be the trove for all the information on the project as the project progresses.

### Issue Tracker
The official project issue tracker for Layerworx Linux will be the GitHub issue tracker currently located [here](https://github.com/layerworx/linux/issues). All issues should be filled out completely and tagged correctly.

### Mailing Lists
We currently have no list, but are accepting corporate sponsorship for hosting services, build servers and mailing list hosting. 

## Special Thanks
Special thanks to the [Linux From Scratch](http://linuxfromscratch.org) project for providing the resources needed to kickstart this project.

Special thanks to [GitHub](http://www.github.com) for hosting this project, supplying us with the free open source repository, issue tracker and wiki.

Special thanks to [@baho-utot](https://github.com/baho-utot) for kickstarting this project with some of the very heavy lifting required to get this started.
