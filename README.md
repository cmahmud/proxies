# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 344
- HTTP: 327 alive / 66 gold
- HTTPS: 222 alive / 14 gold
- SOCKS4: 236 alive / 141 gold
- SOCKS5: 208 alive / 123 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15325
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
