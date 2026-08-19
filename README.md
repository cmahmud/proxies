# SyndProxy private pool

## Current pool

- Alive now: 1287
- Gold now: 480
- HTTP: 462 alive / 133 gold
- HTTPS: 331 alive / 76 gold
- SOCKS4: 231 alive / 124 gold
- SOCKS5: 263 alive / 147 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17277
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
