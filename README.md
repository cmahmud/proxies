# SyndProxy private pool

## Current pool

- Alive now: 784
- Gold now: 396
- HTTP: 216 alive / 71 gold
- HTTPS: 134 alive / 21 gold
- SOCKS4: 207 alive / 141 gold
- SOCKS5: 227 alive / 163 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26032
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
