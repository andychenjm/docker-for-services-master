#
#--------------------------------------------------------------------------
# Image Setup
#--------------------------------------------------------------------------
#

FROM bluepolaris/php72:v1.1.1

#
#--------------------------------------------------------------------------
# Final Touch
#--------------------------------------------------------------------------
#

# Add supervisord.conf
COPY supervisord.conf /etc/supervisor/supervisord.conf


###########################################################################
# superlance for monitor supervisor
###########################################################################

COPY setuptools-0.6c11-py2.7.egg /tmp/setuptools-0.6c11-py2.7.egg
RUN chmod +x /tmp/setuptools-0.6c11-py2.7.egg
RUN /tmp/setuptools-0.6c11-py2.7.egg

ADD superlance-1.0.0.tar.gz /tmp/
RUN cd /tmp/superlance-1.0.0 && python setup.py install

COPY sendEmail /usr/local/bin/sendEmail





###########################################################################
# Crontab
###########################################################################

USER root

COPY ./crontab /etc/cron.d

RUN chmod -R 644 /etc/cron.d


USER root

ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c",  "/etc/supervisor/supervisord.conf"]


RUN usermod -u 1000 www-data
#
#--------------------------------------------------------------------------
# Check PHP version
#--------------------------------------------------------------------------
#

RUN php -v | head -n 1 | grep -q "PHP ${PHP_VERSION}."

#
#--------------------------------------------------------------------------
# Final Touch
#--------------------------------------------------------------------------
#

WORKDIR /etc/supervisor/conf.d/
