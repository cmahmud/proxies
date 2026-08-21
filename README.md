# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 393
- HTTP: 274 alive / 72 gold
- HTTPS: 188 alive / 21 gold
- SOCKS4: 232 alive / 142 gold
- SOCKS5: 226 alive / 158 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29575
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
