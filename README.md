# SyndProxy private pool

## Current pool

- Alive now: 1579
- Gold now: 569
- HTTP: 652 alive / 192 gold
- HTTPS: 429 alive / 88 gold
- SOCKS4: 227 alive / 130 gold
- SOCKS5: 271 alive / 159 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23096
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
