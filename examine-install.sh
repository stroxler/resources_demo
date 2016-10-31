#!/usr/bin/env bash
set -e
set -x

pip uninstall resources_demo -y || true
make install
pushd .. # make sure we get the installed copy!
resources_demo_dir=$(
python << EOF
from __future__ import print_function
import os
import resources_demo
print(os.path.dirname(resources_demo.__file__))
EOF
)
popd
tree "${resources_demo_dir}"
tree /usr/local/resources_demo_external_resources

