# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 397
- HTTP: 85 alive / 60 gold
- HTTPS: 94 alive / 14 gold
- SOCKS4: 171 alive / 164 gold
- SOCKS5: 177 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42937
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
