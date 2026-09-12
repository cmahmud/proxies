# SyndProxy validated proxy pool

## Current pool

- Alive now: 375
- Gold now: 314
- HTTP: 81 alive / 61 gold
- HTTPS: 35 alive / 21 gold
- SOCKS4: 115 alive / 102 gold
- SOCKS5: 144 alive / 130 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49514
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
