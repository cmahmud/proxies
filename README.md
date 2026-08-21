# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 445
- HTTP: 334 alive / 112 gold
- HTTPS: 224 alive / 30 gold
- SOCKS4: 218 alive / 156 gold
- SOCKS5: 242 alive / 147 gold

## Historical pool

- Discovered: 160018
- Ever alive: 30522
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
