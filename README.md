# SyndProxy private pool

## Current pool

- Alive now: 1590
- Gold now: 583
- HTTP: 635 alive / 197 gold
- HTTPS: 425 alive / 94 gold
- SOCKS4: 239 alive / 141 gold
- SOCKS5: 291 alive / 151 gold

## Historical pool

- Discovered: 136251
- Ever alive: 22746
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
