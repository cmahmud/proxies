# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 388
- HTTP: 91 alive / 65 gold
- HTTPS: 77 alive / 13 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43287
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
