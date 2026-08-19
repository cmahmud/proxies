# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 406
- HTTP: 342 alive / 94 gold
- HTTPS: 261 alive / 17 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 325 alive / 147 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21196
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
