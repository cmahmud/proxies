# SyndProxy private pool

## Current pool

- Alive now: 1385
- Gold now: 598
- HTTP: 484 alive / 200 gold
- HTTPS: 383 alive / 96 gold
- SOCKS4: 243 alive / 145 gold
- SOCKS5: 275 alive / 157 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23584
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
