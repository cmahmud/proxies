# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 540
- HTTP: 388 alive / 169 gold
- HTTPS: 242 alive / 92 gold
- SOCKS4: 205 alive / 137 gold
- SOCKS5: 215 alive / 142 gold

## Historical pool

- Discovered: 122387
- Ever alive: 18655
- Ever gold: 727

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
