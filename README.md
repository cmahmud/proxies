# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 406
- HTTP: 112 alive / 62 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38963
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
