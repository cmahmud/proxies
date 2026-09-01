# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 460
- HTTP: 139 alive / 89 gold
- HTTPS: 127 alive / 35 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 197 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46862
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
