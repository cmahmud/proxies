# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 434
- HTTP: 133 alive / 85 gold
- HTTPS: 52 alive / 23 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43665
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
