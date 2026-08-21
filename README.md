# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 372
- HTTP: 260 alive / 86 gold
- HTTPS: 228 alive / 27 gold
- SOCKS4: 188 alive / 121 gold
- SOCKS5: 225 alive / 138 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28840
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
