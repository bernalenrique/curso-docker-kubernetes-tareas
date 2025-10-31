# --- Stage 1: Build
FROM python:3.10-slim AS builder
# Entorno virtual (venv)
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
#Copiar solo el archivo de requisitos
WORKDIR /app
COPY requirements.txt .
#Instalar dependencias en el venv
RUN pip install --no-cache-dir -r requirements.txt


# --- Stage 2: Produccion
FROM python:3.10-alpine AS production
#Labels metadata de la imagen
LABEL version="1.0"
LABEL description="Appy Produccion"
#Variable de entorno puerto
ENV PORT=5000
#curl (HEALTHCHECK)
RUN apk add --no-cache curl
#Cofiguracion usuario non-root 'appyus'
RUN addgroup -S appgroup && adduser -S appyus -G appgroup
WORKDIR /home/appyus/app
#Copiar aplicacion
COPY appy.py .
#Copiar el entorno virtual
COPY --from=builder /opt/venv /opt/venv
#Asignar propiedades
RUN chown -R appyus:appgroup /home/appyus/app /opt/venv
#Cambiar usuario
USER appyus
#Activar el venv para el usuario
ENV PATH="/opt/venv/bin:$PATH"
#Exponer el puerto para el host
EXPOSE $PORT
#HEALTHCHECK
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:$PORT/api/info || exit 1
#Iniciar la aplicacion
CMD ["python", "./appy.py"]
