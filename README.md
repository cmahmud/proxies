# SyndProxy validated proxy pool

## Current pool

- Alive now: 369
- Gold now: 311
- HTTP: 76 alive / 61 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 113 alive / 104 gold
- SOCKS5: 138 alive / 125 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49504
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
