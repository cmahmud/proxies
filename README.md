# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 441
- HTTP: 108 alive / 79 gold
- HTTPS: 86 alive / 33 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44610
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
