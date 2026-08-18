# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 318
- HTTP: 293 alive / 38 gold
- HTTPS: 189 alive / 10 gold
- SOCKS4: 241 alive / 137 gold
- SOCKS5: 228 alive / 133 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14242
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
