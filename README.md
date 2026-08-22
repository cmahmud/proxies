# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 329
- HTTP: 376 alive / 87 gold
- HTTPS: 263 alive / 27 gold
- SOCKS4: 191 alive / 127 gold
- SOCKS5: 190 alive / 88 gold

## Historical pool

- Discovered: 166948
- Ever alive: 32487
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
