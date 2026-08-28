# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 397
- HTTP: 100 alive / 73 gold
- HTTPS: 81 alive / 10 gold
- SOCKS4: 160 alive / 157 gold
- SOCKS5: 171 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43110
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
