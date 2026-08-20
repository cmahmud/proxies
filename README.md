# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 403
- HTTP: 281 alive / 91 gold
- HTTPS: 182 alive / 23 gold
- SOCKS4: 201 alive / 134 gold
- SOCKS5: 211 alive / 155 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27614
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
