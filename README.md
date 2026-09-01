# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 426
- HTTP: 89 alive / 66 gold
- HTTPS: 44 alive / 25 gold
- SOCKS4: 171 alive / 164 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
