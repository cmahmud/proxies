# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 397
- HTTP: 99 alive / 61 gold
- HTTPS: 110 alive / 15 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41425
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
