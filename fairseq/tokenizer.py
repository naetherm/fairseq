# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import re

SPACE_NORMALIZER = re.compile(r"\s+")


def tokenize_line(line, character_level: bool = True):
    line = SPACE_NORMALIZER.sub(" ", line)
    line = line.strip()
    if character_level:
      return list(line)
    else:
      return line.split()
