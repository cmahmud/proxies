# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 428
- HTTP: 286 alive / 96 gold
- HTTPS: 205 alive / 29 gold
- SOCKS4: 212 alive / 144 gold
- SOCKS5: 265 alive / 159 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32548
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
