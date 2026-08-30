# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 418
- HTTP: 136 alive / 79 gold
- HTTPS: 80 alive / 29 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 212 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43973
- Ever gold: 1381

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
