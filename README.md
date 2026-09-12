# SyndProxy validated proxy pool

## Current pool

- Alive now: 363
- Gold now: 314
- HTTP: 78 alive / 61 gold
- HTTPS: 37 alive / 21 gold
- SOCKS4: 111 alive / 104 gold
- SOCKS5: 137 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49503
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
