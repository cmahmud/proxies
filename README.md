# SyndProxy private pool

## Current pool

- Alive now: 1518
- Gold now: 577
- HTTP: 604 alive / 189 gold
- HTTPS: 364 alive / 94 gold
- SOCKS4: 233 alive / 141 gold
- SOCKS5: 317 alive / 153 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22722
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
