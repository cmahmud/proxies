# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 379
- HTTP: 132 alive / 64 gold
- HTTPS: 158 alive / 21 gold
- SOCKS4: 159 alive / 145 gold
- SOCKS5: 178 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39691
- Ever gold: 1301

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
