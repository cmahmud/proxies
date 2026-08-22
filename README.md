# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 407
- HTTP: 310 alive / 92 gold
- HTTPS: 263 alive / 24 gold
- SOCKS4: 226 alive / 138 gold
- SOCKS5: 240 alive / 153 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32078
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
