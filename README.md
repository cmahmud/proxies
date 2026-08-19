# SyndProxy private pool

## Current pool

- Alive now: 1229
- Gold now: 478
- HTTP: 439 alive / 135 gold
- HTTPS: 311 alive / 76 gold
- SOCKS4: 225 alive / 124 gold
- SOCKS5: 254 alive / 143 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17277
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
