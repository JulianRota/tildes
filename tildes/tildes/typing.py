# Copyright (c) 2018 Tildes contributors <code@tildes.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Custom type aliases to use in type annotations."""

from typing import Any, List, Tuple

# types for an ACE (Access Control Entry), and the ACL (Access Control List) of them
AceType = Tuple[str, Any, str]
AclType = List[AceType]
