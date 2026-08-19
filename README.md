# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 372
- HTTP: 304 alive / 65 gold
- HTTPS: 220 alive / 19 gold
- SOCKS4: 219 alive / 127 gold
- SOCKS5: 227 alive / 161 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15672
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
