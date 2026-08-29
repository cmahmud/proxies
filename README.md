# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 386
- HTTP: 83 alive / 57 gold
- HTTPS: 67 alive / 11 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 174 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43474
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
