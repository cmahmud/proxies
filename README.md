# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 448
- HTTP: 133 alive / 90 gold
- HTTPS: 86 alive / 34 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 202 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44201
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
