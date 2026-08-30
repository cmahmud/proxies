# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 431
- HTTP: 118 alive / 79 gold
- HTTPS: 63 alive / 25 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44307
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
