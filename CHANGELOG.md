# Changelog

All notable changes to this project will be documented in this file.

Since version v2306.1 the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
This project (not yet) adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v2312.1

### Added

- added option to add anchor links by wagtail block-id for all custom blocks
- new wagtail richtext image format `Full Width Optimized` to prevent images
  from being downsized and end up blurry

### Fixed

- fixed broken parallax scrolling
- fixed manage.py permissions
- fixed measure_filters not behaving as intended on first click
- fix a brokendevelopment csp rule
- fixed missing language code in homepage link

### Changed

- updated BO js imports according to the newest release
- load fontawesome via script tag
- disable parallax if reduced-motion preference is used
- update babel monorepo to v7.23.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/931
- update dependency lint-staged to v15.1.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/932
- update dependency eslint to v8.54.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/937
- update babel monorepo to v7.23.5 by @renovate in https://github.com/liqd/digitalstrategie/pull/938
- update dependency eslint to v8.55.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/939
- update dependency postcss to v8.4.32 by @renovate in https://github.com/liqd/digitalstrategie/pull/940
- update dependency lint-staged to v15.2.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/941
- update babel monorepo to v7.23.6 by @renovate in https://github.com/liqd/digitalstrategie/pull/946
- update dependency django to v4.2.8 by @renovate in https://github.com/liqd/digitalstrategie/pull/942
- update dependency wagtail to v5.2.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/935
- update dependency pytest-django to v4.7.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/930
- update dependency sentry-sdk to v1.39.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/933
- update dependency isort to v5.13.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/945
- update actions/setup-python action to v5 by @renovate in https://github.com/liqd/digitalstrategie/pull/943
- update eslint packages by @renovate in https://github.com/liqd/digitalstrategie/pull/954

## v2311.2

### Changed

- update dependency stylelint-config-standard-scss to v11.1.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/921
- update dependency eslint to v8.53.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/925

### Fixed

- incorrect search field names for simple german
- exclude search results from the untranslated title field

## v2311.1

### Added

- make more wagtail blocks available on various page types (#7774)
- better block labels and make teaser colours required fixes (#905)
- add check for faulty po files to CI

### Changed

- add https:// to development csp (!824)
- update wagtail from 4.1 to 4.2 (#7759)
- update wagtail from 4.2 to 5.0 (#7759)
  - adapt to changes in the elasticsearch backend (see https://docs.wagtail.org/en/stable/releases/5.0.html#elasticsearch-backend-no-longer-performs-partial-matching-on-search)
  - add SlugInput widget to slug FieldPanels (see https://docs.wagtail.org/en/stable/releases/5.0.html#slug-field-auto-cleaning-now-relies-on-data-attributes)
  - change FieldPanel('title') to TitleFieldPanel('title') (see https://docs.wagtail.org/en/stable/releases/5.0.html#changes-to-title-slug-field-synchronisation)
- update wagtail from 5.0 to 5.1 (#7759)
- update wagtail from 5.0 to 5.2 (#7759)
- Django from 3.2.19 to 4.0 (#7782)
  - apps: remove deprecated app config in apps init
  - settings: LN10N is now enabled by default
  - templates: ifequal not supported
- Django from 4.0 to 4.1 (#7782)
  - apps: added max_length in multiselectfield to fix index error with
    validators[0]=MaxValueMultiFieldValidator(self.max_length)
  - apps: added migration for wagtail custom renditions
- Django from 4.1 to 4.2 (#7782)
  - requirements: update psycopg to v3
- changed CharField to URLField for measure detail website to ensure links works fixes 878
- update to elasticsearch 8
- Pages which are not published or password protected are excluded from the search results (#851, #877)
- make wagtail toolbar sticky by default
- update translations
- update dependency lint-staged to v13.2.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/825
- update dependency webpack to v5.88.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/826
- update dependency eslint to v8.44.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/828
- update babel monorepo to v7.22.6 by @renovate in https://github.com/liqd/digitalstrategie/pull/830
- update dependency stylelint to v15.10.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/832
- update dependency stylelint to v15.10.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/833
- update dependency postcss to v8.4.25 by @renovate in https://github.com/liqd/digitalstrategie/pull/835
- update babel monorepo by @renovate in https://github.com/liqd/digitalstrategie/pull/834
- update dependency babel-loader to v9.1.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/836
- update babel monorepo to v7.22.9 by @renovate in https://github.com/liqd/digitalstrategie/pull/838
- update dependency postcss to v8.4.26 by @renovate in https://github.com/liqd/digitalstrategie/pull/839
- update dependency eslint to v8.45.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/840
- update dependency webpack to v5.88.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/841
- update dependency stylelint to v15.10.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/842
- update dependency sass to v1.64.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/843
- update dependency postcss to v8.4.27 by @renovate in https://github.com/liqd/digitalstrategie/pull/845
- update dependency sass to v1.64.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/846
- update dependency eslint-plugin-import to v2.28.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/847
- update dependency eslint to v8.46.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/848
- update dependency sass to v1.64.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/850
- update babel monorepo to v7.22.10 by @renovate in https://github.com/liqd/digitalstrategie/pull/856
- update dependency sass to v1.65.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/859
- update dependency sass to v1.65.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/860
- update dependency eslint to v8.47.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/862
- update dependency autoprefixer to v10.4.15 by @renovate in https://github.com/liqd/digitalstrategie/pull/863
- update dependency lint-staged to v13.3.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/864
- update babel monorepo by @renovate in https://github.com/liqd/digitalstrategie/pull/866
- update dependency postcss to v8.4.29 by @renovate in https://github.com/liqd/digitalstrategie/pull/867
- update dependency autoprefixer to v10.4.16 by @renovate in https://github.com/liqd/digitalstrategie/pull/873
- update dependency postcss to v8.4.31 by @renovate in https://github.com/liqd/digitalstrategie/pull/874
- update dependency stylelint to v15.10.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/875
- update dependency flake8 to v6.1.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/849
- update dependency psycopg2-binary to v2.9.9 by @renovate in https://github.com/liqd/digitalstrategie/pull/855
- update babel monorepo to v7.23.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/882
- update dependency pytest to v7.4.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/868
- update dependency psycopg2 to v2.9.9 by @renovate in https://github.com/liqd/digitalstrategie/pull/854
- update dependency brotli to v1.1.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/883
- update dependency stylelint to v15.11.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/890
- update dependency sass to v1.69.5 by @renovate in https://github.com/liqd/digitalstrategie/pull/889
- update dependency sentry-sdk to v1.32.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/831
- update dependency webpack to v5.89.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/892
- update dependency webpack-merge to v5.10.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/893
- update eslint packages by @renovate in https://github.com/liqd/digitalstrategie/pull/895
- update dependency whitenoise to v6.6.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/894
- update actions/checkout action to v4 by @renovate in https://github.com/liqd/digitalstrategie/pull/897
- update actions/setup-node action to v4 by @renovate in https://github.com/liqd/digitalstrategie/pull/898
- update dependency stylelint-config-standard-scss to v11 by @renovate in https://github.com/liqd/digitalstrategie/pull/900
- update dependency lint-staged to v15 by @renovate in https://github.com/liqd/digitalstrategie/pull/899
- update dependency pytest-django to v4.6.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/906
- update dependency wagtail-metadata to v5 by @renovate in https://github.com/liqd/digitalstrategie/pull/901
- update dependency django-widget-tweaks to v1.5.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/885
- update dependency django-debug-toolbar to v4.2.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/861
- update dependency sentry-sdk to v1.33.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/911
- update dependency django to v4.2.7 by @renovate in https://github.com/liqd/digitalstrategie/pull/823
- update dependency sentry-sdk to v1.34.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/918

### Fixed

- search results show page title in wrong language (#852)
- restyle hr tag as BO styles break in safari fixes #879
- add BO js urls to script_src for older browsers and add upgrade requests config fixes #844
- change string on search results page fixes #853
- error when switching language on search page
- search: add missing search indices for some model fields
- make search results better by using search with Fuzzy instead of autocomplete
- error json cannot be NULL by setting homepage empty body to {} in an earlier migration

### Removed

- removed the no longer needed ElasticSearchCustomQueryCompiler

## v2306.2 - 2023-06-27

### Added

- add initial changelog (!812)

### Fixed

- fix incorrect measures result count when using filters and search term (#821)

### Changed

- change renovate rules to include new django and wagtail lts versions (!822)
- update dependency stylelint to v15.9.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/818
- update dependency pytest to v7.4.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/820
- update dependency sentry-sdk to v1.26.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/817

## v2306.1 - 2023-06-22

### Fixed

- Pm 2023 06 issues by @philli-m in #813
- homepage: fix title not shown without background image by @goapunk in #812

### Changed

- update dependency sass to v1.63.4 by @renovate in #802
- update dependency webpack to v5.87.0 by @renovate in #804
- update dependency eslint to v8.43.0 by @renovate in #809
- update dependency stylelint to v15.8.0 by @renovate in #810
- update dependency sass to v1.63.5 by @renovate in #814
- update dependency whitenoise to v6.5.0 by @renovate in #808
- update dependency webpack to v5.88.0 by @renovate in #815
- update dependency sass to v1.63.6 by @renovate in #816

# v2306

## What's Changed

- chore(deps): update dependency autoprefixer to v10.4.14 by @renovate in https://github.com/liqd/digitalstrategie/pull/623
- chore(deps): update dependency husky to v8.0.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/624
- chore(deps): update dependency mini-css-extract-plugin to v2.7.5 by @renovate in https://github.com/liqd/digitalstrategie/pull/625
- chore(deps): update dependency postcss to v8.4.21 by @renovate in https://github.com/liqd/digitalstrategie/pull/626
- apps/contrib: make sure lower footer is only loaded if response ok by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/629
- chore(deps): update dependency sentry-sdk to v1.19.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/575
- chore(deps): update dependency webpack-cli to v5 by @renovate in https://github.com/liqd/digitalstrategie/pull/579
- chore(deps): update dependency babel-loader to v9 by @renovate in https://github.com/liqd/digitalstrategie/pull/580
- chore(deps): update dependency flake8 to v6 by @renovate in https://github.com/liqd/digitalstrategie/pull/581
- chore(deps): update dependency elasticsearch to v7.17.9 by @renovate in https://github.com/liqd/digitalstrategie/pull/590
- chore(deps): update dependency isort to v5.12.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/593
- chore(deps): update dependency lint-staged to v13 by @renovate in https://github.com/liqd/digitalstrategie/pull/599
- chore(deps): update dependency django to v3.2.18 by @renovate in https://github.com/liqd/digitalstrategie/pull/604
- chore(deps): update dependency sass-loader to v13.2.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/632
- chore(deps): update dependency stylelint to v14.16.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/633
- requirements: don't use psycopg2-binary on prod by @goapunk in https://github.com/liqd/digitalstrategie/pull/631
- chore(deps): update dependency stylelint-declaration-strict-value to v1.9.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/634
- chore(deps): update dependency terser-webpack-plugin to v5.3.7 by @renovate in https://github.com/liqd/digitalstrategie/pull/635
- chore(deps): update babel monorepo to v7.21.4 by @renovate in https://github.com/liqd/digitalstrategie/pull/637
- chore(deps): update dependency postcss-loader to v7.2.4 by @renovate in https://github.com/liqd/digitalstrategie/pull/639
- metadata: fix error if site doesn't exist by @goapunk in https://github.com/liqd/digitalstrategie/pull/622
- chore(deps): update dependency sass to v1.62.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/641
- chore(deps): update dependency webpack to v5.79.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/643
- chore(deps): update dependency postcss to v8.4.22 by @renovate in https://github.com/liqd/digitalstrategie/pull/647
- use favicons from styleguide by @goapunk in https://github.com/liqd/digitalstrategie/pull/651
- chore(deps): update dependency webpack to v5.80.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/652
- chore(deps): update dependency postcss to v8.4.23 by @renovate in https://github.com/liqd/digitalstrategie/pull/653
- [#7260] apps/measures: add measures oveview page with basic structure create … by @philli-m in https://github.com/liqd/digitalstrategie/pull/649
- Jd 2023 04 improve footer handling by @goapunk in https://github.com/liqd/digitalstrategie/pull/630
- assets/berlin_css: deps: update berlin css files by @philli-m in https://github.com/liqd/digitalstrategie/pull/655
- chore(deps): update dependency webpack-cli to v5.0.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/657
- Jd 2023 04 video entrypoint by @goapunk in https://github.com/liqd/digitalstrategie/pull/654
- apps/home/measures detail page: adding measures detail page and templ… by @khamui in https://github.com/liqd/digitalstrategie/pull/648
- fix js include for video block by @goapunk in https://github.com/liqd/digitalstrategie/pull/659
- chore(deps): update dependency eslint to v8.39.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/658
- [#7260 #7261] add measures details to tile and to filter by @philli-m in https://github.com/liqd/digitalstrategie/pull/656
- chore(deps): update dependency wagtail-metadata to v4.0.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/636
- chore(deps): update dependency flake8-docstrings to v1.7.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/638
- deps: update stylelint 6.1.0 latest useable version by @philli-m in https://github.com/liqd/digitalstrategie/pull/663
- chore(deps): update dependency whitenoise to v6.4.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/644
- chore(deps): update dependency pytest to v7.3.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/640
- apps/measures/detail-page: make styles work for mobile by @khamui in https://github.com/liqd/digitalstrategie/pull/660
- restrict homepage to root page and limit to one by @goapunk in https://github.com/liqd/digitalstrategie/pull/664
- chore(deps): update dependency sass to v1.62.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/668
- add initial content-security-policy by @goapunk in https://github.com/liqd/digitalstrategie/pull/666
- Revert "add initial content-security-policy" by @philli-m in https://github.com/liqd/digitalstrategie/pull/673
- chore(deps): update dependency lint-staged to v13.2.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/675
- chore(deps): update dependency webpack to v5.81.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/676
- Pm 2023 4 checkbox keys by @philli-m in https://github.com/liqd/digitalstrategie/pull/662
- chore(deps): update babel monorepo to v7.21.5 by @renovate in https://github.com/liqd/digitalstrategie/pull/685
- chore(deps): update dependency postcss-loader to v7.3.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/686
- metadata: fix error if request is None by @goapunk in https://github.com/liqd/digitalstrategie/pull/687
- measures/measures_detail_page: add comma between fields and restructure section inline w… by @philli-m in https://github.com/liqd/digitalstrategie/pull/665
- chore(deps): update dependency sib-api-v3-sdk to v7.6.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/642
- chore(deps): update dependency sentry-sdk to v1.21.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/650
- chore(deps): update dependency @babel/core to v7.21.8 by @renovate in https://github.com/liqd/digitalstrategie/pull/690
- add initial content-security-policy by @philli-m in https://github.com/liqd/digitalstrategie/pull/674
- Translations update from LIQD Weblate by @liqd-translator in https://github.com/liqd/digitalstrategie/pull/582
- [7266] helptext to intro image for overview pages by @khamui in https://github.com/liqd/digitalstrategie/pull/689
- [7261] apps/measures/index page: add pagination and filters by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/688
- chore(deps): update dependency wagtail to v4.1.5 by @renovate in https://github.com/liqd/digitalstrategie/pull/691
- chore(deps): update dependency django to v3.2.19 by @renovate in https://github.com/liqd/digitalstrategie/pull/693
- chore(deps): update dependency stylelint to v15 by @renovate in https://github.com/liqd/digitalstrategie/pull/645
- chore(deps): update dependency webpack to v5.82.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/695
- apps/\*/models: add syntax for translating all strings in the wagtail … by @philli-m in https://github.com/liqd/digitalstrategie/pull/694
- chore(deps): update dependency eslint to v8.40.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/702
- chore(deps): update dependency terser-webpack-plugin to v5.3.8 by @renovate in https://github.com/liqd/digitalstrategie/pull/703
- chore(deps): update dependency webpack-cli to v5.1.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/704
- [#7267 #7264] serve nav menu dependent on url and add ls to footer by @philli-m in https://github.com/liqd/digitalstrategie/pull/692
- chore(deps): update dependency sentry-sdk to v1.22.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/701
- apps/\*OverviewPages/templates: check for language_code and in case of… by @khamui in https://github.com/liqd/digitalstrategie/pull/696
- ls header image by @khamui in https://github.com/liqd/digitalstrategie/pull/705
- chore(deps): update dependency sentry-sdk to v1.22.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/707
- chore(deps): update dependency webpack-cli to v5.1.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/708
- [issues] styling issue fixes by @philli-m in https://github.com/liqd/digitalstrategie/pull/697
- chore(deps): update dependency webpack to v5.82.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/716
- search: only show one highlight by @goapunk in https://github.com/liqd/digitalstrategie/pull/715
- apps/measures/fields of action: making links on detail page lead to f… by @khamui in https://github.com/liqd/digitalstrategie/pull/710
- apps/measures/overview: add search by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/709
- chore(deps): update dependency sentry-sdk to v1.23.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/721
- blocks/teaser_block_tiles: using icontiles class instead of teasertil… by @khamui in https://github.com/liqd/digitalstrategie/pull/719
- chore(deps): update dependency stylelint to v15.6.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/726
- use stage captcha, fix csp for captcha by @goapunk in https://github.com/liqd/digitalstrategie/pull/728
- readme: update with local elastic search instructions by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/725
- [7362] add sentences to show search, filters and result count and some measure overview related fixes by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/720
- chore(deps): update dependency terser-webpack-plugin to v5.3.9 by @renovate in https://github.com/liqd/digitalstrategie/pull/733
- chore(deps): update dependency webpack to v5.83.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/732
- chore(deps): update dependency css-loader to v6.7.4 by @renovate in https://github.com/liqd/digitalstrategie/pull/734
- chore(deps): update dependency mini-css-extract-plugin to v2.7.6 by @renovate in https://github.com/liqd/digitalstrategie/pull/735
- Kl 2023 05 issues by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/724
- chore(deps): update dependency webpack-merge to v5.9.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/737
- chore(deps): update dependency eslint to v8.41.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/738
- Pm 2023 5 a11y issue by @philli-m in https://github.com/liqd/digitalstrategie/pull/730
- chore(deps): update dependency sass-loader to v13.3.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/740
- add matomo by @goapunk in https://github.com/liqd/digitalstrategie/pull/717
- chore(deps): update dependency sentry-sdk to v1.23.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/731
- chore(deps): update dependency django-debug-toolbar to v4.1.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/722
- [7360] apps/contrib: use translated fields for meta tags by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/741
- chore(deps): update dependency sentry-sdk to v1.24.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/743
- some tiny issues fixed by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/747
- teaser_block_tilies: ensure link description is shown finishing fixes… by @philli-m in https://github.com/liqd/digitalstrategie/pull/751
- chore(deps): update dependency webpack to v5.84.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/753
- apps/measures: split filtering and pagination to make sure result cou… by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/750
- apps/measures: add filter count - fixes #700 by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/742
- chore(deps): update dependency webpack to v5.84.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/755
- chore(deps): update dependency postcss-loader to v7.3.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/756
- chore(deps): update dependency pytest-cov to v4.1.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/752
- chore(deps): update dependency wagtail to v4.1.6 by @renovate in https://github.com/liqd/digitalstrategie/pull/754
- chore(deps): update babel monorepo by @renovate in https://github.com/liqd/digitalstrategie/pull/758
- chore(deps): update dependency postcss-loader to v7.3.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/759
- chore(deps): update dependency sass-loader to v13.3.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/760
- chore(deps): update dependency postcss to v8.4.24 by @renovate in https://github.com/liqd/digitalstrategie/pull/762
- chore(deps): update dependency css-loader to v6.8.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/761
- Kl 2023 05 issues 3 by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/757
- chore(deps): update dependency @babel/preset-env to v7.22.4 by @renovate in https://github.com/liqd/digitalstrategie/pull/764
- chore(deps): update dependency eslint-config-standard to v17.1.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/765
- [issues] stoy styling and handover issue fixes by @philli-m in https://github.com/liqd/digitalstrategie/pull/763
- [7361] metatags for detail pages by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/748
- chore(deps): update dependency webpack to v5.85.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/770
- Revert "apps/contrib/meta tags: go to parent for meta tags until found" by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/771
- chore(deps): update dependency eslint to v8.42.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/773
- chore(deps): update dependency stylelint to v15.6.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/774
- chore(deps): update dependency webpack-cli to v5.1.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/775
- footer: add parameter to exclude js from the include file by @goapunk in https://github.com/liqd/digitalstrategie/pull/767
- package.json: override cosmiconfig as workaround for segfault, should… by @goapunk in https://github.com/liqd/digitalstrategie/pull/778
- chore(deps): update dependency webpack to v5.85.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/779
- chore(deps): update dependency webpack-cli to v5.1.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/776
- chore(deps): update dependency sentry-sdk to v1.25.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/772
- chore(deps): update dependency stylelint to v15.7.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/781
- \*/models//contrib/mixins: add helptext for metatags and page title ki… by @philli-m in https://github.com/liqd/digitalstrategie/pull/783
- locale: add new strings for translation by @philli-m in https://github.com/liqd/digitalstrategie/pull/782
- translations: don't keep obsolete translations by @goapunk in https://github.com/liqd/digitalstrategie/pull/784
- apps/home/blocks: change char limits for swiper block fixes #729 by @philli-m in https://github.com/liqd/digitalstrategie/pull/785
- locale: add translatable strings by @philli-m in https://github.com/liqd/digitalstrategie/pull/786
- Ks 05 2023 fix language switch by @Rineee in https://github.com/liqd/digitalstrategie/pull/768
- [7361] make metatags go through parents until metatags are found by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/787
- chore(deps): update dependency webpack to v5.86.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/789
- chore(deps): update dependency webpack-cli to v5.1.4 by @renovate in https://github.com/liqd/digitalstrategie/pull/790
- chore(deps): update dependency sass to v1.63.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/791
- chore(deps): update dependency sentry-sdk to v1.25.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/788
- matomo: add missing whitespace in template by @goapunk in https://github.com/liqd/digitalstrategie/pull/792
- Translations update from LIQD Weblate by @liqd-translator in https://github.com/liqd/digitalstrategie/pull/794
- chore(deps): update babel monorepo to v7.22.5 by @renovate in https://github.com/liqd/digitalstrategie/pull/795
- fix various translations by @goapunk in https://github.com/liqd/digitalstrategie/pull/793
- chore(deps): update dependency postcss-loader to v7.3.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/797
- chore(deps): update dependency sass to v1.63.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/796
- chore(deps): update dependency pytest to v7.3.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/798
- chore(deps): update dependency sass-loader to v13.3.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/799
- update translations by @goapunk in https://github.com/liqd/digitalstrategie/pull/800
- Translations update from LIQD Weblate by @liqd-translator in https://github.com/liqd/digitalstrategie/pull/801

**Full Changelog**: https://github.com/liqd/digitalstrategie/compare/v2211.3...v2306

# v2211.3

## What's Changed

- chore(deps): update dependency mini-css-extract-plugin to v2.7.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/578
- chore(deps): update dependency @babel/core to v7.20.5 by @renovate in https://github.com/liqd/digitalstrategie/pull/584
- chore(deps): update dependency mini-css-extract-plugin to v2.7.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/585
- chore(deps): update dependency postcss-loader to v7.0.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/586
- chore(deps): update dependency stylelint to v14.16.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/587
- chore(deps): update dependency mini-css-extract-plugin to v2.7.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/588
- chore(deps): update dependency sass to v1.56.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/591
- chore(deps): update dependency postcss to v8.4.20 by @renovate in https://github.com/liqd/digitalstrategie/pull/592
- chore(deps): update dependency css-loader to v6.7.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/594
- chore(deps): update dependency sass to v1.57.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/596
- Update dependency stylelint-declaration-strict-value to v1.9.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/597
- Update dependency webpack-cli to v4.10.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/598
- chore(deps): update dependency @babel/core to v7.20.12 by @renovate in https://github.com/liqd/digitalstrategie/pull/603
- chore(deps): update dependency wagtail to v4.1.4 by @renovate in https://github.com/liqd/digitalstrategie/pull/571

**Full Changelog**: https://github.com/liqd/digitalstrategie/compare/v2211.2...v2211.3

# v2211.2

## What's Changed

- base.scss: add additional padding to stop bullet point crop fixes #494 by @phillimorland in https://github.com/liqd/digitalstrategie/pull/576

**Full Changelog**: https://github.com/liqd/digitalstrategie/compare/v2211.1...v2211.2

# v2211.1

## What's Changed

- chore(deps): update dependency postcss to v8.4.19 by @renovate in https://github.com/liqd/digitalstrategie/pull/569
- chore(deps): update dependency stylelint to v14.15.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/572
- chore(deps): update dependency css-loader to v6.7.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/573
- base.scss: add important tag to ensure berlin styles are overwritten … by @phillimorland in https://github.com/liqd/digitalstrategie/pull/574

**Full Changelog**: https://github.com/liqd/digitalstrategie/compare/v2211...v2211.1

# v2211

## What's Changed

- settings/renovate: enable updating py packages and adapt to other pro… by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/490
- chore(deps): update dependency postcss to v8.4.16 by @renovate in https://github.com/liqd/digitalstrategie/pull/459
- chore(deps): update dependency husky to v8 by @renovate in https://github.com/liqd/digitalstrategie/pull/437
- fix(deps): update dependency webpack to v5.74.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/441
- chore(deps): update babel monorepo by @renovate in https://github.com/liqd/digitalstrategie/pull/455
- fix(deps): update dependency copy-webpack-plugin to v11 by @renovate in https://github.com/liqd/digitalstrategie/pull/456
- fix(deps): update dependency sass-loader to v13 by @renovate in https://github.com/liqd/digitalstrategie/pull/460
- chore(deps): update dependency django to v3.2.16 by @renovate in https://github.com/liqd/digitalstrategie/pull/491
- fix(deps): update dependency postcss-loader to v7 by @renovate in https://github.com/liqd/digitalstrategie/pull/461
- chore(deps): update dependency stylelint to v14.14.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/464
- chore(deps): update dependency django-cloudflare-push to v0.2.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/499
- chore(deps): update dependency elasticsearch to v7.17.7 by @renovate in https://github.com/liqd/digitalstrategie/pull/500
- fix(deps): update dependency mini-css-extract-plugin to v2.6.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/482
- chore(deps): update dependency lint-staged to v12.5.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/469
- chore(deps): update dependency postcss to v8.4.18 by @renovate in https://github.com/liqd/digitalstrategie/pull/505
- chore(deps): update dependency psycopg2-binary to v2.9.5 by @renovate in https://github.com/liqd/digitalstrategie/pull/506
- chore(deps): update dependency wagtail to v2.16.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/507
- chore(deps): update dependency pytest to v7.2.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/511
- chore(deps): update dependency sib-api-v3-sdk to v7.5.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/513
- chore(deps): update dependency sentry-sdk to v1.10.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/512
- chore(deps): update actions/setup-python action to v4 by @renovate in https://github.com/liqd/digitalstrategie/pull/517
- chore(deps): update dependency flake8 to v5 by @renovate in https://github.com/liqd/digitalstrategie/pull/518
- chore(deps): update dependency lint-staged to v13 by @renovate in https://github.com/liqd/digitalstrategie/pull/519
- fix(deps): update dependency terser-webpack-plugin to v5.3.6 by @renovate in https://github.com/liqd/digitalstrategie/pull/510
- fix(deps): update dependency autoprefixer to v10.4.12 by @renovate in https://github.com/liqd/digitalstrategie/pull/508
- chore(deps): update dependency webpack-cli to v4.10.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/515
- fix(deps): update dependency node-sass to v7.0.3 by @renovate in https://github.com/liqd/digitalstrategie/pull/509
- chore(deps): update dependency stylelint-declaration-strict-value to v1.9.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/514
- chore(deps): update dependency pytest-cov to v4 by @renovate in https://github.com/liqd/digitalstrategie/pull/520
- chore(deps): update dependency stylelint-config-standard-scss to v6 by @renovate in https://github.com/liqd/digitalstrategie/pull/521
- fix(deps): update dependency autoprefixer to v10.4.13 by @renovate in https://github.com/liqd/digitalstrategie/pull/526
- move isort config to file by @goapunk in https://github.com/liqd/digitalstrategie/pull/503
- ci: use node 18 by @goapunk in https://github.com/liqd/digitalstrategie/pull/502
- replace node-sass with sass by @goapunk in https://github.com/liqd/digitalstrategie/pull/504
- chore(deps): update dependency autoprefixer to v10.4.13 by @renovate in https://github.com/liqd/digitalstrategie/pull/529
- chore(deps): update dependency terser-webpack-plugin to v5.3.6 by @renovate in https://github.com/liqd/digitalstrategie/pull/530
- [#6627] deps wagtail3 by @phillimorland in https://github.com/liqd/digitalstrategie/pull/527
- chore(deps): update dependency whitenoise to v6.2.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/516
- [#6627] deps wagtail4 by @phillimorland in https://github.com/liqd/digitalstrategie/pull/528
- chore(deps): update dependency wagtail to v4.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/522
- [#6598] gruenbuch/models: extend oveview page to create index page with migra… by @phillimorland in https://github.com/liqd/digitalstrategie/pull/535
- [#6514] add libs and update webpack by @phillimorland in https://github.com/liqd/digitalstrategie/pull/531
- apps/home: add microsite overview and detail pages and remove bg colo… by @Rineee in https://github.com/liqd/digitalstrategie/pull/536
- Pm 2022 11 detail page by @phillimorland in https://github.com/liqd/digitalstrategie/pull/537
- Ks 2022 11 gruenbuch intro image by @Rineee in https://github.com/liqd/digitalstrategie/pull/538
- [#6514] styleguide fixes after library download by @phillimorland in https://github.com/liqd/digitalstrategie/pull/534
- Update lower footer by @phillimorland in https://github.com/liqd/digitalstrategie/pull/497
- chore(deps): update dependency stylelint to v14.14.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/542
- chore(deps): update dependency babel-loader to v8.3.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/543
- chore(deps): update dependency sass to v1.56.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/545
- assets/ds_block: fix top margin for coloured blocks on pages with hero by @phillimorland in https://github.com/liqd/digitalstrategie/pull/540
- urls: add language prefix to urls by @Rineee in https://github.com/liqd/digitalstrategie/pull/544
- translations: fix wording contact form - fixes #473 by @fuzzylogic2000 in https://github.com/liqd/digitalstrategie/pull/547
- chore(deps): update babel monorepo to v7.20.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/549
- github/ISSUE_TEMPLATE: update issue template and example by @phillimorland in https://github.com/liqd/digitalstrategie/pull/550
- Ks 2022 11 add teaser columns and single to microsite detail page WITH MIGRATION by @Rineee in https://github.com/liqd/digitalstrategie/pull/552
- ds-block: add overwrite for bg coloured blocks w images to ensure eve… by @phillimorland in https://github.com/liqd/digitalstrategie/pull/551
- chore(deps): update dependency husky to v8.0.2 by @renovate in https://github.com/liqd/digitalstrategie/pull/553
- [#6603] home/blocks: add new video block with template by @phillimorland in https://github.com/liqd/digitalstrategie/pull/541
- gruenbuch: add text with image block to gb overview and index WITH MIGRATION by @Rineee in https://github.com/liqd/digitalstrategie/pull/555
- make newsletter-signup view return 404 if not a post request by @goapunk in https://github.com/liqd/digitalstrategie/pull/557
- chore(deps): update dependency sass to v1.56.1 by @renovate in https://github.com/liqd/digitalstrategie/pull/558
- Translations update from LIQD Weblate by @liqd-translator in https://github.com/liqd/digitalstrategie/pull/556
- Pm 2022 11 mobile img by @phillimorland in https://github.com/liqd/digitalstrategie/pull/559
- video_block: add identifyer to function to ensure correct behaviour f… by @phillimorland in https://github.com/liqd/digitalstrategie/pull/561
- [#6604] add captcha to forms by @goapunk in https://github.com/liqd/digitalstrategie/pull/493
- chore(deps): update dependency webpack to v5.75.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/566
- chore(deps): update dependency sass-loader to v13.2.0 by @renovate in https://github.com/liqd/digitalstrategie/pull/567
- fix various translation issues by @goapunk in https://github.com/liqd/digitalstrategie/pull/564
- Translations update from LIQD Weblate by @liqd-translator in https://github.com/liqd/digitalstrategie/pull/568

**Full Changelog**: https://github.com/liqd/digitalstrategie/compare/v2205.1...v2211

# v2205.1

## What's Changed

- fixed translations

**Full Changelog**: https://github.com/liqd/digitalstrategie/compare/v2205...v2205.1

# v2205

## What's Changed

- improved a11y
- added newsletter block
- added single teaser block
- made blocks available on more pages
- change of logo
- smaller style changes and fixes
- updates

**Full Changelog**: https://github.com/liqd/digitalstrategie/compare/v2204...v2205

# v2204

## What's Changed

- apps/home: added choosable link to text with image block
- Implement full-text search with elasticsearch
- Use berlin.de grid and remove bootstrap
- images/logo: replace old logo
- Add correct fonts
- Add theses block
- forms: update structure for a11y and styling and wording to match CI
- add footer from external resource
- adjusting all existing blocks to match CI
- adjusting all existing pages to match CI
- overview-page/intro-image: adding image and using translatable caption
- add alternative and copyright texts to images
- search: improve search results
- Rm old teasers and blocks that do not match CI
- Gruenbuch: change overview and detail page of Grunbuch
- Add editable social media tags to required pages include image
- issue fixing
- Translations

**Full Changelog**: https://github.com/liqd/digitalstrategie/compare/v2111...v2204

# v2111

Second pre-release with:

- Add berlin.de libraries
- Add berlin.de platform header and footer with additional styling
- Add berlin.de breadcrumb nav
- HomePage - add hero, additional blocks and clean up existing ones
- Teaser blocks added for all page types
- Refactr of file names and classes
- Update of grunbuch styling
- Updates including linting
- Add a11y info to nav with setting for contact details
- Add translatable fields
- Add translations
- Add participation and contact form
- Styling of simple page
- Refactor of wagtail fields and page tree
- Logos
- Caption to images
- Styling Overview page
- Refactor titles
- refactor styles with the introduction of berlin.de libraries

# v2110

Initial release with:

- HomePage
- SimplePage (only using RichTextBlock)
- OverviewPage
- DetailPage
- CallToActionBlock used on HomePage
- FaqBlock used on DetailPages and HomePage
- QuoteBlock used on HomePage
- TextWithImageBlock used on HomePage
- 4 TeaserBlocks to be used on OverviewPages
- settings for important pages imprint and data protection policy
- setting for gruenbuch download
- (unstyled) participation form
- (unstyled) contact form
- gruenbuch app with GruenbuchDetail- and IndexPages and extra block GruenbuchFaqBlock
- translatable fields for German, English and Easy German
- MenuSnippets to use in header and footers (footer and content-footer)
- custom images with (translatable) caption
