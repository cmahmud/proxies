# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 406
- HTTP: 112 alive / 64 gold
- HTTPS: 71 alive / 16 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38375
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
