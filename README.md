# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 439
- HTTP: 106 alive / 76 gold
- HTTPS: 85 alive / 34 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 203 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44613
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
