# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 447
- HTTP: 126 alive / 87 gold
- HTTPS: 71 alive / 36 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 209 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44132
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
