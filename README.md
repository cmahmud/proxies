# SyndProxy private pool

## Current pool

- Alive now: 1557
- Gold now: 623
- HTTP: 537 alive / 209 gold
- HTTPS: 434 alive / 117 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 359 alive / 154 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24064
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
