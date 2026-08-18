# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 259
- HTTP: 399 alive / 32 gold
- HTTPS: 169 alive / 4 gold
- SOCKS4: 212 alive / 118 gold
- SOCKS5: 227 alive / 105 gold

## Historical pool

- Discovered: 99105
- Ever alive: 11749
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
