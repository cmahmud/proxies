# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 411
- HTTP: 313 alive / 94 gold
- HTTPS: 202 alive / 28 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 248 alive / 146 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29718
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
