# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 404
- HTTP: 107 alive / 62 gold
- HTTPS: 67 alive / 16 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38377
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
