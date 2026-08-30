# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 432
- HTTP: 136 alive / 89 gold
- HTTPS: 94 alive / 31 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 208 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44013
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
