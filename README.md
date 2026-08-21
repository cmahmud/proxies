# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 406
- HTTP: 261 alive / 89 gold
- HTTPS: 168 alive / 23 gold
- SOCKS4: 226 alive / 147 gold
- SOCKS5: 256 alive / 147 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29114
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
