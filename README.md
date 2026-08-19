# SyndProxy private pool

## Current pool

- Alive now: 1188
- Gold now: 477
- HTTP: 421 alive / 134 gold
- HTTPS: 294 alive / 76 gold
- SOCKS4: 222 alive / 124 gold
- SOCKS5: 251 alive / 143 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17278
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
