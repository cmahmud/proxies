# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 373
- HTTP: 366 alive / 69 gold
- HTTPS: 272 alive / 20 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 232 alive / 142 gold

## Historical pool

- Discovered: 113533
- Ever alive: 16420
- Ever gold: 516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
