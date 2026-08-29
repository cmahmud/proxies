# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 436
- HTTP: 129 alive / 86 gold
- HTTPS: 50 alive / 23 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43665
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
