# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 402
- HTTP: 108 alive / 65 gold
- HTTPS: 80 alive / 19 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 165 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37299
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
