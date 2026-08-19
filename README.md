# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 390
- HTTP: 289 alive / 72 gold
- HTTPS: 215 alive / 13 gold
- SOCKS4: 245 alive / 151 gold
- SOCKS5: 244 alive / 154 gold

## Historical pool

- Discovered: 129307
- Ever alive: 20402
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
