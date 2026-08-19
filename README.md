# SyndProxy private pool

## Current pool

- Alive now: 1175
- Gold now: 387
- HTTP: 366 alive / 90 gold
- HTTPS: 278 alive / 19 gold
- SOCKS4: 237 alive / 137 gold
- SOCKS5: 294 alive / 141 gold

## Historical pool

- Discovered: 133961
- Ever alive: 21641
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
