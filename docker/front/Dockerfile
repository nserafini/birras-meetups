FROM node:10-alpine as builder

COPY ./front/package.json ./front/package-lock.json ./
RUN npm i && mkdir /app && mv ./node_modules ./app
WORKDIR /app
COPY ./front .
RUN $(npm bin)/ng build --prod --output-path=dist


FROM nginx:1.14.1-alpine

RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
