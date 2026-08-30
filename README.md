# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 428
- HTTP: 129 alive / 84 gold
- HTTPS: 80 alive / 32 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44049
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
