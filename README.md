# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 400
- HTTP: 91 alive / 64 gold
- HTTPS: 73 alive / 19 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 171 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43394
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
