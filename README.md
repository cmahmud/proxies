# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 397
- HTTP: 83 alive / 58 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42906
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
