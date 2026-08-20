# SyndProxy private pool

## Current pool

- Alive now: 704
- Gold now: 363
- HTTP: 201 alive / 74 gold
- HTTPS: 105 alive / 19 gold
- SOCKS4: 184 alive / 126 gold
- SOCKS5: 214 alive / 144 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25602
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
