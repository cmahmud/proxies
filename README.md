# SyndProxy private pool

## Current pool

- Alive now: 1229
- Gold now: 498
- HTTP: 377 alive / 121 gold
- HTTPS: 295 alive / 72 gold
- SOCKS4: 259 alive / 154 gold
- SOCKS5: 298 alive / 151 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17030
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
