# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 442
- HTTP: 126 alive / 87 gold
- HTTPS: 49 alive / 26 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43665
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
