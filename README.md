# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 449
- HTTP: 121 alive / 83 gold
- HTTPS: 102 alive / 32 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45643
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
