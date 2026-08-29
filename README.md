# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 437
- HTTP: 134 alive / 86 gold
- HTTPS: 48 alive / 23 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43665
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
