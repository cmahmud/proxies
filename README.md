# SyndProxy validated proxy pool

## Current pool

- Alive now: 390
- Gold now: 315
- HTTP: 92 alive / 66 gold
- HTTPS: 34 alive / 16 gold
- SOCKS4: 124 alive / 106 gold
- SOCKS5: 140 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49533
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
