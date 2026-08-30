# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 425
- HTTP: 107 alive / 75 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44523
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
