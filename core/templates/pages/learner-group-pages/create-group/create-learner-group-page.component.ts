// Copyright 2018 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview Component for the subtopic viewer.
 */

import { Component, OnDestroy, OnInit } from '@angular/core';
import { downgradeComponent } from '@angular/upgrade/static';
import { TranslateService } from '@ngx-translate/core';
import { Subscription } from 'rxjs';

import { AppConstants } from 'app.constants';
import { SubtopicViewerBackendApiService } from 'domain/subtopic_viewer/subtopic-viewer-backend-api.service';
import { SubtopicPageContents } from 'domain/topic/subtopic-page-contents.model';
import { Subtopic } from 'domain/topic/subtopic.model';
import { AlertsService } from 'services/alerts.service';
import { ContextService } from 'services/context.service';
import { UrlService } from 'services/contextual/url.service';
import { WindowDimensionsService } from 'services/contextual/window-dimensions.service';
import { I18nLanguageCodeService, TranslationKeyType } from 'services/i18n-language-code.service';
import { LoaderService } from 'services/loader.service';
import { PageTitleService } from 'services/page-title.service';
import { LearnerGroupPagesConstants } from '../learner-group-pages.constants';
import { LearnerGroupData } from 'domain/learner_group/learner-group.model';

@Component({
  selector: 'oppia-create-learner-group-page',
  templateUrl: './create-learner-group-page.component.html'
})
export class CreateLearnerGroupPageComponent implements OnInit, OnDestroy {
  directiveSubscriptions = new Subscription();
  LEARNER_GROUP_CREATION_SECTION_I18N_IDS = (
    LearnerGroupPagesConstants.LEARNER_GROUP_CREATION_SECTION_I18N_IDS);

  activeSection: string;
  furthestReachedSectionNumber: number = 2;
  learnerGroupTitle: string = '';
  learnerGroupDescription: string = '';
  learnerGroupSubtopicPageIds: string[] = [];
  learnerGroupStoryIds: string[] = [];

  constructor(
    private alertsService: AlertsService,
    private contextService: ContextService,
    private i18nLanguageCodeService: I18nLanguageCodeService,
    private loaderService: LoaderService,
    private pageTitleService: PageTitleService,
    private subtopicViewerBackendApiService: SubtopicViewerBackendApiService,
    private urlService: UrlService,
    private windowDimensionsService: WindowDimensionsService,
    private translateService: TranslateService
  ) {}

  checkMobileView(): boolean {
    return (this.windowDimensionsService.getWidth() < 500);
  }

  isLanguageRTL(): boolean {
    return this.i18nLanguageCodeService.isCurrentLanguageRTL();
  }

  subscribeToOnLangChange(): void {
    this.directiveSubscriptions.add(
      this.translateService.onLangChange.subscribe(() => {
        this.setPageTitle();
      })
    );
  }

  setPageTitle(): void {
    let translatedTitle = this.translateService.instant(
      'I18N_TOPNAV_TEACHER_DASHBOARD');
    this.pageTitleService.setDocumentTitle(translatedTitle);
  }

  setActiveSection(newActiveSectionName: string, sectionNumber: number): void {
    this.activeSection = newActiveSectionName;
    if (this.furthestReachedSectionNumber < sectionNumber) {
      this.furthestReachedSectionNumber = sectionNumber;
    }
  }

  isGroupDetailsNextButtonDisabled(): boolean {
    return (
      !this.learnerGroupTitle ||
      !this.learnerGroupDescription
    );
  }

  updateLearnerGroupTitle(title: string): void {
    this.learnerGroupTitle = title;
  }

  updateLearnerGroupDesc(description: string): void {
    this.learnerGroupDescription = description;
  }

  updateLearnerGroupSubtopics(subtopicPageId: string): void {
    this.learnerGroupSubtopicPageIds.push(subtopicPageId);
  }

  updateLearnerGroupStories(storyId: string): void {
    this.learnerGroupStoryIds.push(storyId);
  }

  isAddSyllabusNextButtonDisabled(): boolean {
    return (
      !this.learnerGroupStoryIds.length &&
      !this.learnerGroupSubtopicPageIds.length
    );
  }

  getProgressTabStatusClass(sectionNumber: number): string {
    if (sectionNumber < this.furthestReachedSectionNumber) {
      return 'completed';
    }
    if (sectionNumber === this.furthestReachedSectionNumber) {
      return 'active';
    }
  }

  ngOnInit(): void {
    console.log('testing')
    this.activeSection = (
      this.LEARNER_GROUP_CREATION_SECTION_I18N_IDS.ADD_STUDENTS
    );
    // this.loaderService.showLoadingScreen('Loading');
  }

  ngOnDestroy(): void {
    this.directiveSubscriptions.unsubscribe();
    this.contextService.removeCustomEntityContext();
  }
}

angular.module('oppia').directive(
  'oppiaCreateLearnerGroupPage',
  downgradeComponent({component: CreateLearnerGroupPageComponent}));