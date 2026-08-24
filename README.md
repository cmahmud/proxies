# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 432
- HTTP: 126 alive / 80 gold
- HTTPS: 105 alive / 23 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34041
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
