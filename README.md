# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 357
- HTTP: 317 alive / 71 gold
- HTTPS: 231 alive / 12 gold
- SOCKS4: 204 alive / 129 gold
- SOCKS5: 244 alive / 145 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20361
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
