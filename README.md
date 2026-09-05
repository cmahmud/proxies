# SyndProxy validated proxy pool

## Current pool

- Alive now: 376
- Gold now: 300
- HTTP: 107 alive / 81 gold
- HTTPS: 34 alive / 19 gold
- SOCKS4: 77 alive / 66 gold
- SOCKS5: 158 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47857
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
