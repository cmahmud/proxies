# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 300
- HTTP: 347 alive / 64 gold
- HTTPS: 277 alive / 19 gold
- SOCKS4: 210 alive / 114 gold
- SOCKS5: 212 alive / 103 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15560
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
