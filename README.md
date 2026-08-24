# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 435
- HTTP: 133 alive / 78 gold
- HTTPS: 129 alive / 25 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34356
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
