# SyndProxy validated proxy pool

## Current pool

- Alive now: 397
- Gold now: 314
- HTTP: 90 alive / 66 gold
- HTTPS: 42 alive / 16 gold
- SOCKS4: 127 alive / 106 gold
- SOCKS5: 138 alive / 126 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49540
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
