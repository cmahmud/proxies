# SyndProxy private pool

## Current pool

- Alive now: 1390
- Gold now: 606
- HTTP: 522 alive / 199 gold
- HTTPS: 404 alive / 99 gold
- SOCKS4: 218 alive / 145 gold
- SOCKS5: 246 alive / 163 gold

## Historical pool

- Discovered: 138953
- Ever alive: 23400
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
