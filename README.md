# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 397
- HTTP: 79 alive / 52 gold
- HTTPS: 50 alive / 19 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41683
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
