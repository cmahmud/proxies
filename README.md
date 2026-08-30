# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 425
- HTTP: 102 alive / 74 gold
- HTTPS: 60 alive / 23 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 202 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44463
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
