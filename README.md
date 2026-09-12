# SyndProxy validated proxy pool

## Current pool

- Alive now: 387
- Gold now: 314
- HTTP: 88 alive / 64 gold
- HTTPS: 34 alive / 16 gold
- SOCKS4: 123 alive / 105 gold
- SOCKS5: 142 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49527
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
