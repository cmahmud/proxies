# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 516
- HTTP: 367 alive / 152 gold
- HTTPS: 242 alive / 90 gold
- SOCKS4: 210 alive / 133 gold
- SOCKS5: 211 alive / 141 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19892
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
