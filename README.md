# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 412
- HTTP: 320 alive / 107 gold
- HTTPS: 189 alive / 28 gold
- SOCKS4: 219 alive / 131 gold
- SOCKS5: 234 alive / 146 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30640
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
