# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 388
- HTTP: 105 alive / 67 gold
- HTTPS: 89 alive / 18 gold
- SOCKS4: 170 alive / 149 gold
- SOCKS5: 182 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39317
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
