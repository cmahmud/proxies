# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 426
- HTTP: 366 alive / 98 gold
- HTTPS: 274 alive / 24 gold
- SOCKS4: 236 alive / 146 gold
- SOCKS5: 274 alive / 158 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28137
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
