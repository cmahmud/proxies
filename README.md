# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 437
- HTTP: 107 alive / 82 gold
- HTTPS: 65 alive / 24 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44562
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
