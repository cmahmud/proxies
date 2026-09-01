# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 472
- HTTP: 139 alive / 92 gold
- HTTPS: 127 alive / 44 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46960
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
