# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 368
- HTTP: 322 alive / 78 gold
- HTTPS: 239 alive / 11 gold
- SOCKS4: 213 alive / 127 gold
- SOCKS5: 225 alive / 152 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20385
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
