# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 390
- HTTP: 393 alive / 109 gold
- HTTPS: 264 alive / 29 gold
- SOCKS4: 213 alive / 117 gold
- SOCKS5: 281 alive / 135 gold

## Historical pool

- Discovered: 152223
- Ever alive: 27993
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
