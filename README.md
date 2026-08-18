# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 250
- HTTP: 185 alive / 35 gold
- HTTPS: 129 alive / 8 gold
- SOCKS4: 221 alive / 125 gold
- SOCKS5: 210 alive / 82 gold

## Historical pool

- Discovered: 94324
- Ever alive: 9349
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
