// Copyright 2020 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview Backend api service for user exploration permissions.
 */

import { downgradeInjectable } from '@angular/upgrade/static';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { ContextService } from 'services/context.service';
import { UrlInterpolationService } from
  'domain/utilities/url-interpolation.service';
import { TransientCheckpointUrl, TransientCheckpointUrlBackendDict } from
  'domain/exploration/transient-checkpoint-url.model';

@Injectable({
  providedIn: 'root'
})
export class TransientCheckpointUrlBackendApiService {
  constructor(
    private contextService: ContextService,
    private http: HttpClient,
    private urlInterpolationService: UrlInterpolationService) {}

  async getTransientCheckpointUrlAsync(): Promise<TransientCheckpointUrl> {
    let transientCheckpointUrl = this.urlInterpolationService
      .interpolateUrl('/progress/<unique_progress_id>', {
        progress_url_id: this.contextService.getProgressUrlId()
      });

    return new Promise((resolve, reject) => {
      this.http.get<TransientCheckpointUrlBackendDict>(
        transientCheckpointUrl).toPromise().then(response => {
        let permissionsObject = (
          TransientCheckpointUrl.createFromBackendDict(
            response));
        resolve(permissionsObject);
      }, errorResponse => {
        reject(errorResponse.error.error);
      });
    });
  }

  async recordTransientCheckpointUrlAsync(
    transientCheckpointData: TransientCheckpointUrlBackendDict
  ): Promise<TransientCheckpointUrl> {

    let transientCheckpointUrl = this.urlInterpolationService
      .interpolateUrl('/progress/<unique_progress_id>', {
        progress_url_id: this.contextService.getProgressUrlId()
      });

    return new Promise((resolve, reject) => {
      this.http.post<TransientCheckpointUrlBackendDict>(
        transientCheckpointUrl, transientCheckpointData).toPromise().then(
          response => {
            let transientCheckpointUrlDict = (
              TransientCheckpointUrl.createFromBackendDict(
                response));
            resolve(transientCheckpointUrlDict);
          }, errorResponse => {
            reject(errorResponse.error.error);
          }
        );
    });
  }
}

angular.module('oppia').factory(
  'TransientCheckpointUrlBackendApiService',
  downgradeInjectable(TransientCheckpointUrlBackendApiService));
