# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 388
- HTTP: 73 alive / 54 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 176 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42888
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
