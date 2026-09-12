# SyndProxy validated proxy pool

## Current pool

- Alive now: 404
- Gold now: 322
- HTTP: 99 alive / 65 gold
- HTTPS: 39 alive / 20 gold
- SOCKS4: 120 alive / 105 gold
- SOCKS5: 146 alive / 132 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49519
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
