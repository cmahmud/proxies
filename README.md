# SyndProxy private pool

## Current pool

- Alive now: 603
- Gold now: 226
- HTTP: 162 alive / 25 gold
- HTTPS: 78 alive / 7 gold
- SOCKS4: 162 alive / 112 gold
- SOCKS5: 201 alive / 82 gold

## Historical pool

- Discovered: 91696
- Ever alive: 8392
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
