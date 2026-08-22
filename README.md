# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 405
- HTTP: 271 alive / 93 gold
- HTTPS: 216 alive / 32 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 236 alive / 133 gold

## Historical pool

- Discovered: 161987
- Ever alive: 31297
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
