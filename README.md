# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 448
- HTTP: 320 alive / 95 gold
- HTTPS: 226 alive / 31 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 273 alive / 172 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31032
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
