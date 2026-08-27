# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 397
- HTTP: 91 alive / 54 gold
- HTTPS: 54 alive / 19 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41687
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
