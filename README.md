# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 444
- HTTP: 132 alive / 84 gold
- HTTPS: 70 alive / 28 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43695
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
