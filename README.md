# SyndProxy private pool

## Current pool

- Alive now: 651
- Gold now: 241
- HTTP: 167 alive / 27 gold
- HTTPS: 98 alive / 8 gold
- SOCKS4: 196 alive / 119 gold
- SOCKS5: 190 alive / 87 gold

## Historical pool

- Discovered: 86739
- Ever alive: 6883
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
