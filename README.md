# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 416
- HTTP: 326 alive / 84 gold
- HTTPS: 244 alive / 16 gold
- SOCKS4: 227 alive / 158 gold
- SOCKS5: 288 alive / 158 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21843
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
