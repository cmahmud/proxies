# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 404
- HTTP: 86 alive / 61 gold
- HTTPS: 62 alive / 19 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38541
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
