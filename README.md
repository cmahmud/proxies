# SyndProxy private pool

## Current pool

- Alive now: 1391
- Gold now: 452
- HTTP: 510 alive / 111 gold
- HTTPS: 385 alive / 33 gold
- SOCKS4: 238 alive / 149 gold
- SOCKS5: 258 alive / 159 gold

## Historical pool

- Discovered: 160009
- Ever alive: 30502
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
