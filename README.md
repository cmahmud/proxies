# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 401
- HTTP: 182 alive / 80 gold
- HTTPS: 152 alive / 20 gold
- SOCKS4: 205 alive / 151 gold
- SOCKS5: 230 alive / 150 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27510
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
