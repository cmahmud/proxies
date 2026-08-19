# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 404
- HTTP: 365 alive / 76 gold
- HTTPS: 244 alive / 14 gold
- SOCKS4: 275 alive / 157 gold
- SOCKS5: 248 alive / 157 gold

## Historical pool

- Discovered: 131412
- Ever alive: 20679
- Ever gold: 873

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
