
FROM python:3.12-slim

# Update operating system packages
RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/ .

# Remove unnecessary Python packaging tools
RUN python -m pip uninstall -y pip setuptools && \
    useradd --system --no-create-home appuser

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
