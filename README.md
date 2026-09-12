# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 330
- HTTP: 83 alive / 66 gold
- HTTPS: 30 alive / 19 gold
- SOCKS4: 132 alive / 115 gold
- SOCKS5: 143 alive / 130 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49548
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
