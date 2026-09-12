# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 447
- HTTP: 126 alive / 88 gold
- HTTPS: 59 alive / 30 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49311
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
