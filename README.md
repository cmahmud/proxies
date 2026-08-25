# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 395
- HTTP: 92 alive / 65 gold
- HTTPS: 88 alive / 17 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 164 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37462
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
