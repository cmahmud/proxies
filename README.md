# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 403
- HTTP: 286 alive / 92 gold
- HTTPS: 194 alive / 31 gold
- SOCKS4: 227 alive / 154 gold
- SOCKS5: 222 alive / 126 gold

## Historical pool

- Discovered: 160987
- Ever alive: 30869
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
