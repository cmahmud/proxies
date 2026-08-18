# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 251
- HTTP: 187 alive / 36 gold
- HTTPS: 138 alive / 8 gold
- SOCKS4: 219 alive / 124 gold
- SOCKS5: 205 alive / 83 gold

## Historical pool

- Discovered: 94324
- Ever alive: 9349
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
