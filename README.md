# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 571
- HTTP: 307 alive / 188 gold
- HTTPS: 232 alive / 97 gold
- SOCKS4: 230 alive / 136 gold
- SOCKS5: 239 alive / 150 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23247
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
