# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 397
- HTTP: 78 alive / 57 gold
- HTTPS: 68 alive / 18 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42877
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
