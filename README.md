# SyndProxy private pool

## Current pool

- Alive now: 1302
- Gold now: 406
- HTTP: 424 alive / 92 gold
- HTTPS: 326 alive / 11 gold
- SOCKS4: 254 alive / 143 gold
- SOCKS5: 298 alive / 160 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21054
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
