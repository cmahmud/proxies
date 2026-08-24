# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 391
- HTTP: 96 alive / 59 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33503
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
