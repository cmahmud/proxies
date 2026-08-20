# SyndProxy private pool

## Current pool

- Alive now: 699
- Gold now: 376
- HTTP: 190 alive / 72 gold
- HTTPS: 119 alive / 19 gold
- SOCKS4: 189 alive / 140 gold
- SOCKS5: 201 alive / 145 gold

## Historical pool

- Discovered: 147186
- Ever alive: 25820
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
