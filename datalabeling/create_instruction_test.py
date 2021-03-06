#!/usr/bin/env python

# Copyright 2019 Google, Inc
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

import os

import create_instruction
from google.cloud import datalabeling_v1beta1 as datalabeling
import pytest

PROJECT_ID = os.getenv('GCLOUD_PROJECT')
INSTRUCTION_GCS_URI = ('gs://cloud-samples-data/datalabeling'
                       '/instruction/test.pdf')


@pytest.mark.slow
def test_create_instruction(capsys):
    result = create_instruction.create_instruction(
        PROJECT_ID,
        'IMAGE',
        INSTRUCTION_GCS_URI
    )
    out, _ = capsys.readouterr()
    assert 'The instruction resource name: ' in out

    # Delete the created instruction.
    instruction_name = result.name
    client = datalabeling.DataLabelingServiceClient()
    client.delete_instruction(instruction_name)
