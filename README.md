# SyndProxy private pool

## Current pool

- Alive now: 1242
- Gold now: 405
- HTTP: 446 alive / 104 gold
- HTTPS: 284 alive / 25 gold
- SOCKS4: 217 alive / 130 gold
- SOCKS5: 295 alive / 146 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22583
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
