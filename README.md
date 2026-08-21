# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 434
- HTTP: 401 alive / 109 gold
- HTTPS: 265 alive / 30 gold
- SOCKS4: 233 alive / 151 gold
- SOCKS5: 248 alive / 144 gold

## Historical pool

- Discovered: 160018
- Ever alive: 30515
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
