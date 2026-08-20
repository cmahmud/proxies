# SyndProxy private pool

## Current pool

- Alive now: 1515
- Gold now: 604
- HTTP: 620 alive / 198 gold
- HTTPS: 419 alive / 94 gold
- SOCKS4: 223 alive / 146 gold
- SOCKS5: 253 alive / 166 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23100
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
