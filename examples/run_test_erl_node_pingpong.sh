#! /bin/sh

# A test case for testing packing/unpacking of erlang-terms:
#
# A message is sent from an erlang node to a python node.
# That message is echoed back to the erlang node, which checks
# if the received message matches the original message.
#

erl=${ERL:-erl}

# First make sure epmd is up and running. (needed by the python-node)
$erl -noinput -detach -sname ensure_epmd_started@localhost -s erlang halt

# Now start the pythonnode
PYTHONPATH=..:$PYTHONPATH ./test_erl_node_pingpong.py \
    -n ss1@localhost -c 123456 \
	 > test_erl_node_pingpong.log-py 2>&1 &
pynode=$!

$erl -noinput -sname enode1@localhost \
    -setcookie 123456 \
    -s test_erl_node_pingpong start \
    -s erlang halt

kill $pynode
