# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 379
- HTTP: 91 alive / 57 gold
- HTTPS: 53 alive / 22 gold
- SOCKS4: 156 alive / 150 gold
- SOCKS5: 163 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43645
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
