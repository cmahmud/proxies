# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 447
- HTTP: 137 alive / 90 gold
- HTTPS: 84 alive / 33 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 200 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44201
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
