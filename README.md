# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 370
- HTTP: 354 alive / 82 gold
- HTTPS: 286 alive / 20 gold
- SOCKS4: 190 alive / 117 gold
- SOCKS5: 244 alive / 151 gold

## Historical pool

- Discovered: 158230
- Ever alive: 29903
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
