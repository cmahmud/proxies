# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 427
- HTTP: 124 alive / 83 gold
- HTTPS: 81 alive / 32 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44048
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
