# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 432
- HTTP: 109 alive / 79 gold
- HTTPS: 51 alive / 25 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 197 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44523
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
