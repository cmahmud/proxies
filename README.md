# SyndProxy private pool

## Current pool

- Alive now: 1267
- Gold now: 479
- HTTP: 455 alive / 133 gold
- HTTPS: 325 alive / 76 gold
- SOCKS4: 229 alive / 124 gold
- SOCKS5: 258 alive / 146 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17277
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
