# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.4] Unreleased [Github Repo]
## [0.0.3] - 30-06-2020 
### Added
- `follow` and `rfollow` modes to read periodically from services readables characteristics
- `get_stag`, `get_scode`, `get_ctag`, `get_ccode`, `get_aptag`, `get_apcode`,
`get_mtag`, `get_mcode` to get services, characteristics, appearances, and manufacturers names/tags and codes
- `cmdata` to get characteristic metadata (name, type, uuid, unit, format, notes...). (Not all characteristics are available yet)
- `-r` and `-mdata` options for `get_services`command to read and get characteristic metadata
- `dmdata` to get descriptor metadata
### Fix
- put, get commands in BLE SHELL-REPL
- git commands in BLE SHELL-REPL
## [0.0.2] - 23-05-2020
### Fix
- BLE SHELL-REPL WIP
## [0.0.1] - 20-05-2020
### Added
- Initial release and register in PYPI
