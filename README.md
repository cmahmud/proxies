# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 411
- HTTP: 324 alive / 94 gold
- HTTPS: 203 alive / 22 gold
- SOCKS4: 222 alive / 135 gold
- SOCKS5: 257 alive / 160 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32432
- Ever gold: 1181

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
