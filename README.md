# SyndProxy private pool

## Current pool

- Alive now: 1391
- Gold now: 409
- HTTP: 481 alive / 79 gold
- HTTPS: 335 alive / 16 gold
- SOCKS4: 252 alive / 157 gold
- SOCKS5: 323 alive / 157 gold

## Historical pool

- Discovered: 134532
- Ever alive: 21951
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
