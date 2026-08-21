# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 417
- HTTP: 294 alive / 89 gold
- HTTPS: 201 alive / 25 gold
- SOCKS4: 216 alive / 140 gold
- SOCKS5: 239 alive / 163 gold

## Historical pool

- Discovered: 159203
- Ever alive: 30169
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
