# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 538
- HTTP: 454 alive / 180 gold
- HTTPS: 257 alive / 110 gold
- SOCKS4: 191 alive / 118 gold
- SOCKS5: 186 alive / 130 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19408
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
