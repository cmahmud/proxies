# SyndProxy private pool

## Current pool

- Alive now: 1141
- Gold now: 375
- HTTP: 436 alive / 83 gold
- HTTPS: 265 alive / 23 gold
- SOCKS4: 166 alive / 104 gold
- SOCKS5: 274 alive / 165 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32468
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
