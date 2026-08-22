# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 404
- HTTP: 341 alive / 86 gold
- HTTPS: 216 alive / 25 gold
- SOCKS4: 230 alive / 150 gold
- SOCKS5: 250 alive / 143 gold

## Historical pool

- Discovered: 165619
- Ever alive: 32283
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
