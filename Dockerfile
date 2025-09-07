FROM busybox
WORKDIR /site
COPY dist/ .
CMD ["httpd", "-f", "-p", "80", "-h", "/site"]