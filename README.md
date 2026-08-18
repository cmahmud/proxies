# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 348
- HTTP: 288 alive / 52 gold
- HTTPS: 177 alive / 14 gold
- SOCKS4: 206 alive / 133 gold
- SOCKS5: 222 alive / 149 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14910
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
