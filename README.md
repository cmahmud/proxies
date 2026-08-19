# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 306
- HTTP: 348 alive / 64 gold
- HTTPS: 229 alive / 19 gold
- SOCKS4: 216 alive / 117 gold
- SOCKS5: 198 alive / 106 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15593
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
