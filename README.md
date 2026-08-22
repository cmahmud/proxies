# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 405
- HTTP: 309 alive / 93 gold
- HTTPS: 239 alive / 29 gold
- SOCKS4: 250 alive / 148 gold
- SOCKS5: 251 alive / 135 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31316
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
