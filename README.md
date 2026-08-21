# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 368
- HTTP: 357 alive / 82 gold
- HTTPS: 280 alive / 20 gold
- SOCKS4: 184 alive / 116 gold
- SOCKS5: 242 alive / 150 gold

## Historical pool

- Discovered: 158230
- Ever alive: 29903
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
