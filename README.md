# SyndProxy validated proxy pool

## Current pool

- Alive now: 401
- Gold now: 322
- HTTP: 82 alive / 66 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 120 alive / 105 gold
- SOCKS5: 154 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49493
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
