# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 324
- HTTP: 84 alive / 63 gold
- HTTPS: 40 alive / 23 gold
- SOCKS4: 118 alive / 108 gold
- SOCKS5: 147 alive / 130 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49500
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
