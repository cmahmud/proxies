# SyndProxy private pool

## Current pool

- Alive now: 1213
- Gold now: 408
- HTTP: 449 alive / 91 gold
- HTTPS: 253 alive / 17 gold
- SOCKS4: 233 alive / 143 gold
- SOCKS5: 278 alive / 157 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20868
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
