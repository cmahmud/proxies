# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 398
- HTTP: 93 alive / 66 gold
- HTTPS: 77 alive / 15 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 168 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43411
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
