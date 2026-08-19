# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 358
- HTTP: 320 alive / 70 gold
- HTTPS: 214 alive / 13 gold
- SOCKS4: 217 alive / 128 gold
- SOCKS5: 225 alive / 147 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20331
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
