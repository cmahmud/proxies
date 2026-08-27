# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 401
- HTTP: 94 alive / 60 gold
- HTTPS: 54 alive / 16 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41646
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
