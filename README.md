# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 398
- HTTP: 379 alive / 102 gold
- HTTPS: 271 alive / 24 gold
- SOCKS4: 203 alive / 129 gold
- SOCKS5: 303 alive / 143 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22609
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
