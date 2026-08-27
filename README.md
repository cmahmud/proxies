# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 399
- HTTP: 95 alive / 56 gold
- HTTPS: 107 alive / 15 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41501
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
