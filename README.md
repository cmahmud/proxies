# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 457
- HTTP: 139 alive / 85 gold
- HTTPS: 114 alive / 34 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 191 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46719
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
