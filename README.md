# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 516
- HTTP: 326 alive / 159 gold
- HTTPS: 252 alive / 89 gold
- SOCKS4: 202 alive / 141 gold
- SOCKS5: 201 alive / 127 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18403
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
