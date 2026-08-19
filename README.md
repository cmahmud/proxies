# SyndProxy private pool

## Current pool

- Alive now: 801
- Gold now: 309
- HTTP: 236 alive / 59 gold
- HTTPS: 161 alive / 11 gold
- SOCKS4: 212 alive / 115 gold
- SOCKS5: 192 alive / 124 gold

## Historical pool

- Discovered: 129264
- Ever alive: 20144
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
