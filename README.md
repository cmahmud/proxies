# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 445
- HTTP: 130 alive / 87 gold
- HTTPS: 135 alive / 24 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42235
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
