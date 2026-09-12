# SyndProxy validated proxy pool

## Current pool

- Alive now: 391
- Gold now: 314
- HTTP: 90 alive / 65 gold
- HTTPS: 36 alive / 18 gold
- SOCKS4: 118 alive / 104 gold
- SOCKS5: 147 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49527
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
