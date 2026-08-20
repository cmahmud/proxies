# SyndProxy private pool

## Current pool

- Alive now: 697
- Gold now: 379
- HTTP: 195 alive / 68 gold
- HTTPS: 100 alive / 17 gold
- SOCKS4: 190 alive / 138 gold
- SOCKS5: 212 alive / 156 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25813
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
