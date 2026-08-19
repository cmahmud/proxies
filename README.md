# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 459
- HTTP: 361 alive / 118 gold
- HTTPS: 269 alive / 73 gold
- SOCKS4: 222 alive / 139 gold
- SOCKS5: 218 alive / 129 gold

## Historical pool

- Discovered: 113545
- Ever alive: 16591
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
