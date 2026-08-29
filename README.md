# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 389
- HTTP: 82 alive / 64 gold
- HTTPS: 77 alive / 11 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 170 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43424
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
