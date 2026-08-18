# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 252
- HTTP: 175 alive / 36 gold
- HTTPS: 119 alive / 8 gold
- SOCKS4: 214 alive / 125 gold
- SOCKS5: 205 alive / 83 gold

## Historical pool

- Discovered: 94325
- Ever alive: 9349
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
