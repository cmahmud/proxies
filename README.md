# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 427
- HTTP: 118 alive / 80 gold
- HTTPS: 61 alive / 24 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 208 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44336
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
