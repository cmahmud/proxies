# SyndProxy private pool

## Current pool

- Alive now: 1102
- Gold now: 537
- HTTP: 391 alive / 158 gold
- HTTPS: 274 alive / 89 gold
- SOCKS4: 227 alive / 158 gold
- SOCKS5: 210 alive / 132 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18224
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
