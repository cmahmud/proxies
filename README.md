# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 444
- HTTP: 124 alive / 90 gold
- HTTPS: 81 alive / 30 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44288
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
