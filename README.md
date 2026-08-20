# SyndProxy private pool

## Current pool

- Alive now: 1522
- Gold now: 633
- HTTP: 518 alive / 212 gold
- HTTPS: 426 alive / 113 gold
- SOCKS4: 232 alive / 148 gold
- SOCKS5: 346 alive / 160 gold

## Historical pool

- Discovered: 141233
- Ever alive: 24114
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
