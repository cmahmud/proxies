# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 436
- HTTP: 115 alive / 80 gold
- HTTPS: 58 alive / 29 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44301
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
