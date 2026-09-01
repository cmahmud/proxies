# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 416
- HTTP: 91 alive / 62 gold
- HTTPS: 44 alive / 22 gold
- SOCKS4: 170 alive / 164 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
