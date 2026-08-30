# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 425
- HTTP: 139 alive / 81 gold
- HTTPS: 75 alive / 32 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 249 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43904
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
