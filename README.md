# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 439
- HTTP: 326 alive / 110 gold
- HTTPS: 215 alive / 27 gold
- SOCKS4: 214 alive / 135 gold
- SOCKS5: 256 alive / 167 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30647
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
