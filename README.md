# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 423
- HTTP: 104 alive / 63 gold
- HTTPS: 74 alive / 21 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 217 alive / 178 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35895
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
