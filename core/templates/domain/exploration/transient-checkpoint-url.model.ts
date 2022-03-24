// Copyright 2022 The Oppia Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * @fileoverview Frontend model for transient checkpoint url.
 */

export interface TransientCheckpointUrlBackendDict {
  'exploration_id': string;
  'unique_progress_url_id': string;
  'last_completed_checkpoint_state_name': string;
  'latest_visited_checkpoint_state_name': string;
}

export class TransientCheckpointUrl {
  explorationId: string;
  uniqueProgressUrlId: string;
  lastCompletedCheckpointStateName: string;
  latestVisitedCheckpointStateName: string;

  constructor(
      explorationId: string,
      uniqueProgressUrlId: string,
      lastCompletedCheckpointStateName: string,
      latestVisitedCheckpointStateName: string
    ) {
    this.explorationId = explorationId;
    this.uniqueProgressUrlId = uniqueProgressUrlId;
    this.lastCompletedCheckpointStateName = lastCompletedCheckpointStateName;
    this.latestVisitedCheckpointStateName = latestVisitedCheckpointStateName;
  }

  static createFromBackendDict(
      backendDict: TransientCheckpointUrlBackendDict): TransientCheckpointUrl {
    return new TransientCheckpointUrl(
      backendDict.exploration_id, backendDict.unique_progress_url_id,
      backendDict.last_completed_checkpoint_state_name,
      backendDict.latest_visited_checkpoint_state_name);
  }
}
