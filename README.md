# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 402
- HTTP: 361 alive / 98 gold
- HTTPS: 216 alive / 20 gold
- SOCKS4: 223 alive / 132 gold
- SOCKS5: 255 alive / 152 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27946
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
