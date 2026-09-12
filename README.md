# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 332
- HTTP: 81 alive / 63 gold
- HTTPS: 32 alive / 18 gold
- SOCKS4: 129 alive / 117 gold
- SOCKS5: 146 alive / 134 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49548
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
