# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 439
- HTTP: 125 alive / 85 gold
- HTTPS: 47 alive / 26 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43665
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
