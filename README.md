# SyndProxy validated proxy pool

## Current pool

- Alive now: 393
- Gold now: 317
- HTTP: 86 alive / 64 gold
- HTTPS: 34 alive / 17 gold
- SOCKS4: 125 alive / 105 gold
- SOCKS5: 148 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49523
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
