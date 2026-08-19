# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 399
- HTTP: 316 alive / 75 gold
- HTTPS: 245 alive / 14 gold
- SOCKS4: 255 alive / 151 gold
- SOCKS5: 254 alive / 159 gold

## Historical pool

- Discovered: 131105
- Ever alive: 20541
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
