# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 340
- HTTP: 300 alive / 60 gold
- HTTPS: 193 alive / 14 gold
- SOCKS4: 202 alive / 142 gold
- SOCKS5: 182 alive / 124 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20182
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
