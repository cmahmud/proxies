# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 429
- HTTP: 298 alive / 110 gold
- HTTPS: 194 alive / 37 gold
- SOCKS4: 219 alive / 137 gold
- SOCKS5: 233 alive / 145 gold

## Historical pool

- Discovered: 160263
- Ever alive: 30733
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
