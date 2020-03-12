#!/bin/bash

# elasticsearch 生产模式 vm.max_map_count 设置

sysctl -w vm.max_map_count=262144