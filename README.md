# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 417
- HTTP: 101 alive / 74 gold
- HTTPS: 132 alive / 20 gold
- SOCKS4: 182 alive / 157 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42104
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
