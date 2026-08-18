# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 275
- HTTP: 266 alive / 52 gold
- HTTPS: 178 alive / 11 gold
- SOCKS4: 213 alive / 110 gold
- SOCKS5: 218 alive / 102 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14447
- Ever gold: 463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
