# SyndProxy private pool

## Current pool

- Alive now: 1555
- Gold now: 642
- HTTP: 596 alive / 212 gold
- HTTPS: 480 alive / 109 gold
- SOCKS4: 229 alive / 151 gold
- SOCKS5: 250 alive / 170 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23968
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
