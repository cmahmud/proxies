# SyndProxy private pool

## Current pool

- Alive now: 1246
- Gold now: 419
- HTTP: 459 alive / 103 gold
- HTTPS: 319 alive / 31 gold
- SOCKS4: 224 alive / 153 gold
- SOCKS5: 244 alive / 132 gold

## Historical pool

- Discovered: 159263
- Ever alive: 30344
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
