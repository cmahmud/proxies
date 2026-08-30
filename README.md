# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 439
- HTTP: 127 alive / 85 gold
- HTTPS: 73 alive / 28 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44292
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
