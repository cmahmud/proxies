# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 432
- HTTP: 149 alive / 89 gold
- HTTPS: 94 alive / 31 gold
- SOCKS4: 160 alive / 152 gold
- SOCKS5: 207 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44012
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
