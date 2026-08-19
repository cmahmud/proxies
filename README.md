# SyndProxy private pool

## Current pool

- Alive now: 1141
- Gold now: 498
- HTTP: 387 alive / 123 gold
- HTTPS: 247 alive / 74 gold
- SOCKS4: 238 alive / 150 gold
- SOCKS5: 269 alive / 151 gold

## Historical pool

- Discovered: 114411
- Ever alive: 17020
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
