# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 314
- HTTP: 88 alive / 63 gold
- HTTPS: 37 alive / 18 gold
- SOCKS4: 118 alive / 104 gold
- SOCKS5: 146 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49527
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
