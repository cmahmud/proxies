# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 428
- HTTP: 119 alive / 81 gold
- HTTPS: 63 alive / 21 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44312
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
