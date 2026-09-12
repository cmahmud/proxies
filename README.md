# SyndProxy validated proxy pool

## Current pool

- Alive now: 401
- Gold now: 325
- HTTP: 80 alive / 63 gold
- HTTPS: 43 alive / 22 gold
- SOCKS4: 123 alive / 108 gold
- SOCKS5: 155 alive / 132 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49499
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
