# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 417
- HTTP: 248 alive / 77 gold
- HTTPS: 169 alive / 24 gold
- SOCKS4: 229 alive / 154 gold
- SOCKS5: 227 alive / 162 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27391
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
