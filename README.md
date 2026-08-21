# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 406
- HTTP: 371 alive / 107 gold
- HTTPS: 233 alive / 26 gold
- SOCKS4: 226 alive / 132 gold
- SOCKS5: 235 alive / 141 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30597
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
