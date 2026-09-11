# SyndProxy validated proxy pool

## Current pool

- Alive now: 439
- Gold now: 352
- HTTP: 119 alive / 82 gold
- HTTPS: 47 alive / 23 gold
- SOCKS4: 82 alive / 75 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48647
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
