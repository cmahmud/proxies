# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 398
- HTTP: 83 alive / 57 gold
- HTTPS: 44 alive / 15 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42832
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
