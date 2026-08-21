# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 408
- HTTP: 319 alive / 94 gold
- HTTPS: 280 alive / 19 gold
- SOCKS4: 216 alive / 150 gold
- SOCKS5: 246 alive / 145 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29274
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
