# SyndProxy validated proxy pool

## Current pool

- Alive now: 401
- Gold now: 326
- HTTP: 80 alive / 62 gold
- HTTPS: 41 alive / 23 gold
- SOCKS4: 126 alive / 108 gold
- SOCKS5: 154 alive / 133 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49497
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
