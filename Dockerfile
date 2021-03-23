#
#   IBM Containerized Forecasting Workflow
#
#    Licensed Materials - Property of IBM
#    “Restricted Materials of IBM”
#     Copyright IBM Corp. 2017 ALL RIGHTS RESERVED

FROM centos:centos7
RUN mkdir /opt/deepthunder; \
mkdir /opt/deepthunder/data
ADD build.sh /opt/deepthunder/
ADD loadenv.sh /opt/deepthunder/
ADD externalDependencies /opt/deepthunder/externalDependencies/

RUN yum -y install epel-release; \
yum update -y ; \
yum -y install ksh bc ncompress pkgconfig jasper jasper-devel cairo cairo-devel python-devel curl-devel expat expat-devel zlib zlib-devel file sudo wget bzip2 tar gzip gcc-gfortran byacc zip python unzip yasm libXext-devel mpich mpich-devel make bison patch libpng libpng-devel libtool automake autoconf flex flex-devel tcsh bzip2-devel time xz libffi-devel xz-libs libcurl-devel curl sqlite-devel python-setuptools gcc-c++ wgrib2 wgrib2-devel hdf5 hdf5-devel netcdf netcdf-devel netcdf-fortran netcdf-fortran-devel grib_api grib_api-devel nco nco-devel ncl which python-pip; \
easy_install pip=20.3.3; \
pip install argparse; \
pip install pytz; \
cd /opt/deepthunder && /bin/bash loadenv.sh && /bin/bash build.sh; \
yum remove -y jasper-devel cairo-devel grib_api-devel python-devel curl-devel expat-devel zlib-devel gcc-gfortran byacc yasm libXext-devel mpich-devel libpng-devel libtool automake autoconf flex flex-devel bzip2-devel libcurl-devel sqlite-devel python-setuptools gcc-c++ hdf5-devel netcdf-fortran-devel nco-devel java libstdc++-devel glibc-devel libxcb-devel libquadmath-devel libXfixes-devel libXdamage-devel libdrm-devel glib2-devel libffi-devel xorg-x11-proto-devel libXau-devel pixman-devel libjpeg-turbo-devel libX11-devel libXrender-devel ;\
yum clean all ;\
yum -y install netcdf4-python ncview;\
rm -rf /usr/share/ncarg/data/cdf

ADD PreProcessing /opt/deepthunder/PreProcessing/
ADD stevedore /opt/deepthunder/stevedore/
ADD run_simulation.py /opt/deepthunder/run_simulation.py

#Add MPICH to the PATH
ENV PATH /usr/lib64/mpich/bin:$PATH

#if it exists copy over precompiled wrf.exe with its accompanying features
ADD featurePack/* /opt/deepthunder/externalDependencies/WRF/

#Added this after having problems verifying certificates in unit testing
CMD /usr/bin/echo "check_certificate = off" >> ~/.wgetrc
