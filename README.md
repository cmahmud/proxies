# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 396
- HTTP: 339 alive / 83 gold
- HTTPS: 198 alive / 27 gold
- SOCKS4: 227 alive / 134 gold
- SOCKS5: 253 alive / 152 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32421
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
