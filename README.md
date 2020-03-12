# php environment

## install

```shell
cp .env.example .env

docker-compose build php-fpm
docker-compose build nginx
docker-compose build php-worker
docker-compose build rabbitmq

docker-compose up -d  php-fpm nginx php-worker rabbitmq
```

## Tips

> Linux中启动ElasticSearch

启动ElasticSearch生产模式，要先设置  `vm.max_map_count` 为 `262144`

```shell
sudo sysctl -w vm.max_map_count=262144
```

或者修改`/etc/sysctl.conf`文件，添加`vm.max_map_count=262144`
