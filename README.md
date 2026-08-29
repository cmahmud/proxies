# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 372
- HTTP: 91 alive / 66 gold
- HTTPS: 84 alive / 15 gold
- SOCKS4: 159 alive / 149 gold
- SOCKS5: 170 alive / 142 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43340
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
