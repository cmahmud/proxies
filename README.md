# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 421
- HTTP: 91 alive / 66 gold
- HTTPS: 71 alive / 25 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45476
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
