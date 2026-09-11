# SyndProxy validated proxy pool

## Current pool

- Alive now: 439
- Gold now: 364
- HTTP: 116 alive / 87 gold
- HTTPS: 37 alive / 27 gold
- SOCKS4: 84 alive / 76 gold
- SOCKS5: 202 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48647
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
