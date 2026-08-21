# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 381
- HTTP: 284 alive / 90 gold
- HTTPS: 227 alive / 29 gold
- SOCKS4: 175 alive / 124 gold
- SOCKS5: 219 alive / 138 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28860
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
