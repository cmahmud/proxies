# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 477
- HTTP: 369 alive / 122 gold
- HTTPS: 239 alive / 72 gold
- SOCKS4: 221 alive / 140 gold
- SOCKS5: 256 alive / 143 gold

## Historical pool

- Discovered: 114270
- Ever alive: 16918
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
