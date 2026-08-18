# SyndProxy private pool

## Current pool

- Alive now: 759
- Gold now: 249
- HTTP: 186 alive / 35 gold
- HTTPS: 137 alive / 8 gold
- SOCKS4: 226 alive / 124 gold
- SOCKS5: 210 alive / 82 gold

## Historical pool

- Discovered: 94324
- Ever alive: 9349
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
