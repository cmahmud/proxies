# SyndProxy validated proxy pool

## Current pool

- Alive now: 374
- Gold now: 311
- HTTP: 79 alive / 60 gold
- HTTPS: 41 alive / 21 gold
- SOCKS4: 114 alive / 105 gold
- SOCKS5: 140 alive / 125 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49506
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
