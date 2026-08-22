# SyndProxy private pool

## Current pool

- Alive now: 809
- Gold now: 365
- HTTP: 247 alive / 91 gold
- HTTPS: 160 alive / 30 gold
- SOCKS4: 176 alive / 105 gold
- SOCKS5: 226 alive / 139 gold

## Historical pool

- Discovered: 167356
- Ever alive: 32559
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
