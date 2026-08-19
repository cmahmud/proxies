# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 345
- HTTP: 361 alive / 65 gold
- HTTPS: 210 alive / 15 gold
- SOCKS4: 241 alive / 141 gold
- SOCKS5: 210 alive / 124 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15325
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
