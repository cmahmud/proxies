# SyndProxy validated proxy pool

## Current pool

- Alive now: 369
- Gold now: 205
- HTTP: 111 alive / 46 gold
- HTTPS: 66 alive / 8 gold
- SOCKS4: 74 alive / 65 gold
- SOCKS5: 118 alive / 86 gold

## Historical pool

- Discovered: 169854
- Ever alive: 32702
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
