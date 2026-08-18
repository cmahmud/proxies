# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 324
- HTTP: 247 alive / 38 gold
- HTTPS: 162 alive / 9 gold
- SOCKS4: 220 alive / 143 gold
- SOCKS5: 220 alive / 134 gold

## Historical pool

- Discovered: 103330
- Ever alive: 13996
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
