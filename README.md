# SyndProxy private pool

## Current pool

- Alive now: 1223
- Gold now: 425
- HTTP: 400 alive / 105 gold
- HTTPS: 304 alive / 30 gold
- SOCKS4: 202 alive / 125 gold
- SOCKS5: 317 alive / 165 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24855
- Ever gold: 1050

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
