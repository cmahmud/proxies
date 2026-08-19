# SyndProxy private pool

## Current pool

- Alive now: 1341
- Gold now: 396
- HTTP: 479 alive / 97 gold
- HTTPS: 327 alive / 22 gold
- SOCKS4: 216 alive / 133 gold
- SOCKS5: 319 alive / 144 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22510
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
