# SyndProxy private pool

## Current pool

- Alive now: 1098
- Gold now: 420
- HTTP: 350 alive / 87 gold
- HTTPS: 260 alive / 15 gold
- SOCKS4: 246 alive / 156 gold
- SOCKS5: 242 alive / 162 gold

## Historical pool

- Discovered: 131719
- Ever alive: 20764
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
