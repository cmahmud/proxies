# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 347
- HTTP: 344 alive / 64 gold
- HTTPS: 208 alive / 15 gold
- SOCKS4: 242 alive / 143 gold
- SOCKS5: 214 alive / 125 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15325
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
