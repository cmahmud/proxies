# SyndProxy private pool

## Current pool

- Alive now: 1282
- Gold now: 398
- HTTP: 425 alive / 91 gold
- HTTPS: 287 alive / 15 gold
- SOCKS4: 254 alive / 147 gold
- SOCKS5: 316 alive / 145 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21692
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
