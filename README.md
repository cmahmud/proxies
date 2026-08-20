# SyndProxy private pool

## Current pool

- Alive now: 802
- Gold now: 381
- HTTP: 219 alive / 79 gold
- HTTPS: 168 alive / 19 gold
- SOCKS4: 208 alive / 134 gold
- SOCKS5: 207 alive / 149 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27186
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
