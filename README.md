# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 403
- HTTP: 119 alive / 69 gold
- HTTPS: 62 alive / 17 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38942
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
