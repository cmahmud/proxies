# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 391
- HTTP: 322 alive / 98 gold
- HTTPS: 224 alive / 20 gold
- SOCKS4: 188 alive / 127 gold
- SOCKS5: 278 alive / 146 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22533
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
