# SyndProxy validated proxy pool

## Current pool

- Alive now: 397
- Gold now: 323
- HTTP: 79 alive / 61 gold
- HTTPS: 43 alive / 22 gold
- SOCKS4: 123 alive / 108 gold
- SOCKS5: 152 alive / 132 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49500
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
