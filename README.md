# SyndProxy validated proxy pool

## Current pool

- Alive now: 402
- Gold now: 318
- HTTP: 97 alive / 66 gold
- HTTPS: 39 alive / 18 gold
- SOCKS4: 124 alive / 106 gold
- SOCKS5: 142 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49544
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
