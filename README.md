# SyndProxy private pool

## Current pool

- Alive now: 647
- Gold now: 251
- HTTP: 159 alive / 36 gold
- HTTPS: 85 alive / 7 gold
- SOCKS4: 206 alive / 124 gold
- SOCKS5: 197 alive / 84 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9353
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
