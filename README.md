# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 372
- HTTP: 335 alive / 69 gold
- HTTPS: 247 alive / 19 gold
- SOCKS4: 227 alive / 142 gold
- SOCKS5: 224 alive / 142 gold

## Historical pool

- Discovered: 113533
- Ever alive: 16394
- Ever gold: 516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
