# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 419
- HTTP: 297 alive / 90 gold
- HTTPS: 196 alive / 20 gold
- SOCKS4: 229 alive / 148 gold
- SOCKS5: 272 alive / 161 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22330
- Ever gold: 896

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
