FROM nginx:1.27-alpine

# Nginx leerá estas envs en tiempo de ejecución
ENV ESTUDIANTES_URL=""
ENV CARRERAS_URL=""
ENV FACULTADES_URL=""

# Copiamos el conf
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080
