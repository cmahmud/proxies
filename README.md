# SyndProxy private pool

## Current pool

- Alive now: 1870
- Gold now: 650
- HTTP: 731 alive / 234 gold
- HTTPS: 619 alive / 115 gold
- SOCKS4: 224 alive / 145 gold
- SOCKS5: 296 alive / 156 gold

## Historical pool

- Discovered: 142693
- Ever alive: 24284
- Ever gold: 981

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
