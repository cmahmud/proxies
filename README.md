# SyndProxy validated proxy pool

## Current pool

- Alive now: 403
- Gold now: 322
- HTTP: 88 alive / 64 gold
- HTTPS: 46 alive / 23 gold
- SOCKS4: 120 alive / 105 gold
- SOCKS5: 149 alive / 130 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49495
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
