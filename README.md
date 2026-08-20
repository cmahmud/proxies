# SyndProxy private pool

## Current pool

- Alive now: 1539
- Gold now: 594
- HTTP: 625 alive / 195 gold
- HTTPS: 431 alive / 90 gold
- SOCKS4: 229 alive / 144 gold
- SOCKS5: 254 alive / 165 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23100
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
