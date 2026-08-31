# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 457
- HTTP: 120 alive / 87 gold
- HTTPS: 99 alive / 38 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 204 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45605
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
