# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 397
- HTTP: 82 alive / 65 gold
- HTTPS: 103 alive / 10 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43052
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
