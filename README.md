# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 398
- HTTP: 369 alive / 97 gold
- HTTPS: 269 alive / 21 gold
- SOCKS4: 207 alive / 130 gold
- SOCKS5: 299 alive / 150 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22522
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
