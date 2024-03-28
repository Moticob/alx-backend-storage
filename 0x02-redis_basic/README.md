0x02. Redis Basic
This repository contains solutions for the Redis Basic project, which is a part of the ALX Back-end program. The project focuses on using Redis for basic operations and simple caching.

Requirements
All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
Use pycodestyle style (version 2.5)
All modules, classes, and functions should have documentation
All functions and methods should have type-annotations
Install Redis on Ubuntu 18.04:
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
Use Redis in a container
Redis server is stopped by default - when starting a container, start it with: service redis-server start
Learning Objectives
Learn how to use Redis for basic operations
Learn how to use Redis as a simple cache
Resources
Redis Crash Course Tutorial
Redis commands
Redis python client
How to Use Redis With Python
Tasks
0. Writing strings to Redis
Create a Cache class with a store method that takes data, generates a random key, stores the input data in Redis using the random key, and returns the key.

Type-annotate store correctly
Data can be a str, bytes, int, or float
1. Reading from Redis and recovering original type
Create a get method that takes a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

Conserve the original Redis.get behavior if the key does not exist
Implement 2 new methods: get_str and get_int that will automatically parametrize Cache.get with the correct conversion function
2. Incrementing values
Create a count_calls decorator that takes a single method Callable argument and returns a Callable. Increment the count for that key every time the method is called and return the value returned by the original method.

3. Storing lists
Create a call_history decorator that stores the history of inputs and outputs for a particular function.

Use the decorated function's qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively
Use rpush to append the input arguments and store the output using rpush in the "...:outputs" list, then return the output
4. Retrieving lists
Implement a replay function to display the history of calls of a particular function.

Use keys generated in previous tasks to generate the output
5. Implementing an expiring web cache and tracker (Advanced)
Implement a get_page function that caches the result with an expiration time of 10 seconds.

Use http://slowwly.robertomurray.co.uk to simulate a slow response and test your caching
Bonus: implement this use case with decorators
