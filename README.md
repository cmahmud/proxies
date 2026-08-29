# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 397
- HTTP: 96 alive / 66 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 169 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43450
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
