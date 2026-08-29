# SyndProxy validated proxy pool

## Current pool

- Alive now: 425
- Gold now: 365
- HTTP: 57 alive / 42 gold
- HTTPS: 37 alive / 7 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 169 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43549
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
