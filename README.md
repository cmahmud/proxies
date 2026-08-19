# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 360
- HTTP: 326 alive / 74 gold
- HTTPS: 236 alive / 11 gold
- SOCKS4: 227 alive / 126 gold
- SOCKS5: 234 alive / 149 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20278
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
