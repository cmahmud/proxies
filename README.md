# SyndProxy private pool

## Current pool

- Alive now: 1524
- Gold now: 587
- HTTP: 535 alive / 195 gold
- HTTPS: 458 alive / 91 gold
- SOCKS4: 238 alive / 145 gold
- SOCKS5: 293 alive / 156 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24050
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
