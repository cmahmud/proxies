# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 427
- HTTP: 116 alive / 80 gold
- HTTPS: 61 alive / 21 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44312
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
