# flake8: noqa
#!/usr/bin/env python
# coding=utf-8
# Copyright 2021 The HuggingFace Inc. team. All rights reserved.
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
# limitations under the License

from . import tqdm as _tqdm  # _tqdm is the module
from ._cache_assets import cached_assets_path
from ._cache_manager import (
    CachedFileInfo,
    CachedRepoInfo,
    CachedRevisionInfo,
    CacheNotFound,
    CorruptedCacheException,
    DeleteCacheStrategy,
    HFCacheInfo,
    scan_cache_dir,
)
from ._chunk_utils import chunk_iterable
from ._datetime import parse_datetime
from ._errors import (
    BadRequestError,
    EntryNotFoundError,
    GatedRepoError,
    HfHubHTTPError,
    LocalEntryNotFoundError,
    RepositoryNotFoundError,
    RevisionNotFoundError,
    hf_raise_for_status,
)
from ._fixes import SoftTemporaryDirectory, yaml_dump
from ._git_credential import list_credential_helpers, set_git_credential, unset_git_credential
from ._headers import build_hf_headers, get_token_to_send
from ._hf_folder import HfFolder
from ._http import configure_http_backend, get_session, http_backoff
from ._paths import filter_repo_objects, IGNORE_GIT_FOLDER_PATTERNS
from ._runtime import (
    dump_environment_info,
    get_fastai_version,
    get_fastcore_version,
    get_graphviz_version,
    get_hf_hub_version,
    get_hf_transfer_version,
    get_jinja_version,
    get_pillow_version,
    get_pydot_version,
    get_python_version,
    get_tf_version,
    get_torch_version,
    is_fastai_available,
    is_fastcore_available,
    is_google_colab,
    is_graphviz_available,
    is_hf_transfer_available,
    is_jinja_available,
    is_notebook,
    is_pillow_available,
    is_pydot_available,
    is_tf_available,
    is_torch_available,
)
from ._subprocess import run_interactive_subprocess, run_subprocess
from ._validators import (
    HFValidationError,
    smoothly_deprecate_use_auth_token,
    validate_hf_hub_args,
    validate_repo_id,
)
from .tqdm import (
    are_progress_bars_disabled,
    disable_progress_bars,
    enable_progress_bars,
    tqdm,
    tqdm_stream_file,
)
from ._telemetry import send_telemetry
