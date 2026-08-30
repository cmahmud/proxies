# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 446
- HTTP: 134 alive / 87 gold
- HTTPS: 71 alive / 35 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 203 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44235
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
