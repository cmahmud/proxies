# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 402
- HTTP: 256 alive / 77 gold
- HTTPS: 189 alive / 19 gold
- SOCKS4: 208 alive / 146 gold
- SOCKS5: 251 alive / 160 gold

## Historical pool

- Discovered: 155790
- Ever alive: 29325
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
