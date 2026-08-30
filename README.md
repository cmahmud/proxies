# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 447
- HTTP: 131 alive / 89 gold
- HTTPS: 54 alive / 30 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43673
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
