# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 402
- HTTP: 104 alive / 60 gold
- HTTPS: 75 alive / 14 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 199 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38297
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
