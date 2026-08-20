# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 404
- HTTP: 229 alive / 74 gold
- HTTPS: 146 alive / 20 gold
- SOCKS4: 222 alive / 152 gold
- SOCKS5: 228 alive / 158 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26030
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
