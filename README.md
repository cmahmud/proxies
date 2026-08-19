# SyndProxy private pool

## Current pool

- Alive now: 1470
- Gold now: 438
- HTTP: 516 alive / 93 gold
- HTTPS: 364 alive / 27 gold
- SOCKS4: 263 alive / 149 gold
- SOCKS5: 327 alive / 169 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22465
- Ever gold: 901

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
