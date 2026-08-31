# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 484
- HTTP: 139 alive / 102 gold
- HTTPS: 120 alive / 46 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45070
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
