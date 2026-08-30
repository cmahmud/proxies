# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 441
- HTTP: 117 alive / 79 gold
- HTTPS: 84 alive / 33 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44622
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
