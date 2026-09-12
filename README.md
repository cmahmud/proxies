# SyndProxy validated proxy pool

## Current pool

- Alive now: 385
- Gold now: 314
- HTTP: 89 alive / 66 gold
- HTTPS: 32 alive / 15 gold
- SOCKS4: 124 alive / 105 gold
- SOCKS5: 140 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49527
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
