# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 402
- HTTP: 397 alive / 76 gold
- HTTPS: 259 alive / 12 gold
- SOCKS4: 288 alive / 150 gold
- SOCKS5: 263 alive / 164 gold

## Historical pool

- Discovered: 131117
- Ever alive: 20673
- Ever gold: 872

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
