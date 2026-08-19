# SyndProxy private pool

## Current pool

- Alive now: 790
- Gold now: 337
- HTTP: 246 alive / 59 gold
- HTTPS: 156 alive / 12 gold
- SOCKS4: 202 alive / 144 gold
- SOCKS5: 186 alive / 122 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20156
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
