# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 323
- HTTP: 83 alive / 64 gold
- HTTPS: 43 alive / 23 gold
- SOCKS4: 124 alive / 106 gold
- SOCKS5: 149 alive / 130 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49496
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
