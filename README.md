# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 374
- HTTP: 203 alive / 77 gold
- HTTPS: 182 alive / 17 gold
- SOCKS4: 200 alive / 149 gold
- SOCKS5: 185 alive / 131 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25928
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
