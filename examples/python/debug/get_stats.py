# Copyright 2019 The gRPC Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Poll statistics from the server."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import argparse
import grpc

# TODO(https://github.com/grpc/grpc/issues/19863): Remove.
try:
    from src.python.grpcio_channelz.grpc_channelz.v1 import channelz_pb2
    from src.python.grpcio_channelz.grpc_channelz.v1 import channelz_pb2_grpc
except ImportError:
    from grpc_channelz.v1 import channelz_pb2
    from grpc_channelz.v1 import channelz_pb2_grpc


def run(addr):
    with grpc.insecure_channel(addr) as channel:
        channelz_stub = channelz_pb2_grpc.ChannelzStub(channel)
        response = channelz_stub.GetServers(
            channelz_pb2.GetServersRequest(start_server_id=0))
        print('Info for all servers: %s' % response)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--addr',
        nargs=1,
        type=str,
        default='[::]:50051',
        help='the address to request')
    args = parser.parse_args()
    run(addr=args.addr)


if __name__ == '__main__':
    logging.basicConfig()
    main()
