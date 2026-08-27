# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 397
- HTTP: 81 alive / 47 gold
- HTTPS: 49 alive / 18 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41674
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
