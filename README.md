# SyndProxy private pool

## Current pool

- Alive now: 1404
- Gold now: 591
- HTTP: 550 alive / 194 gold
- HTTPS: 357 alive / 96 gold
- SOCKS4: 233 alive / 140 gold
- SOCKS5: 264 alive / 161 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23134
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
