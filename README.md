# SyndProxy private pool

## Current pool

- Alive now: 1137
- Gold now: 394
- HTTP: 400 alive / 92 gold
- HTTPS: 272 alive / 14 gold
- SOCKS4: 214 alive / 128 gold
- SOCKS5: 251 alive / 160 gold

## Historical pool

- Discovered: 131843
- Ever alive: 21246
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
