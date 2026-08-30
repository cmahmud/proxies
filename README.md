# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 439
- HTTP: 103 alive / 76 gold
- HTTPS: 84 alive / 34 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44611
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
