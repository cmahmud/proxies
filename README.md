# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 421
- HTTP: 93 alive / 59 gold
- HTTPS: 71 alive / 34 gold
- SOCKS4: 188 alive / 160 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45493
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
