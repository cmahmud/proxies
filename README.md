# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 404
- HTTP: 97 alive / 67 gold
- HTTPS: 74 alive / 20 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 170 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37283
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
