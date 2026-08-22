# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 333
- HTTP: 304 alive / 83 gold
- HTTPS: 227 alive / 26 gold
- SOCKS4: 201 alive / 138 gold
- SOCKS5: 189 alive / 86 gold

## Historical pool

- Discovered: 167104
- Ever alive: 32512
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
