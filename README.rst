resources_demo: looking at how to have resource files in pip packages
=====================================================================

This package has some internal data inside of the
resources_demo python package directory, and also an external
resource in the resources_demo_external_resources directory.

Internal resources: data files within a package
-----------------------------------------------

The internal resources can be added by working with
`package_data` in the `setup.py` file. In my example I use maximal glob
expansion to avoid listing paths, but it's entirely possible to put
much more specific glob strings, or paths to individual files, inside
of the lists in this dict.

The important semantic thing here is that each entry is a list of file
glob strings associated with a specific package, and

Also, a critically important detail that isn't clear from reading the internet
is that you *cannot* use `package_data` and also set
`include_package_data=True`, I have a branch of this repo confirming that
if you do this the data won't even make it into the tarball. I think this is
probably a conceptual bug in distutils, and it isn't even documented, but
it's something you need to be aware of.


External resources: data files not in a package
-----------------------------------------------

The only place pip knows how to install external resources is on
your system `$PREFIX`. In order to declare these external resources,
add them to MANIFEST.in.

Here we recursively include all files
`resources_demo_external_resources` in MANIFEST.in, so they wind up
inside of `$PREFIX/resources_demo_external_resources`;
for example on my OSX machine they wind up in
`/usr/local/resources_demo_external_resources`.

In most cases you should probably prefer internal resources for ordinary
python programs and use `package_data` to get them, but if you have
a python package associated with sysadmin (for example a tool such as
`supervisorctl`, which is a python-based daemon manager) then it might
be appropriate to use external resources and MANIFEST.in.
