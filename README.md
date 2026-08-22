# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 407
- HTTP: 263 alive / 93 gold
- HTTPS: 156 alive / 18 gold
- SOCKS4: 221 alive / 136 gold
- SOCKS5: 248 alive / 160 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32433
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
