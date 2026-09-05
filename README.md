# SyndProxy validated proxy pool

## Current pool

- Alive now: 376
- Gold now: 291
- HTTP: 107 alive / 77 gold
- HTTPS: 42 alive / 19 gold
- SOCKS4: 72 alive / 65 gold
- SOCKS5: 155 alive / 130 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47885
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
