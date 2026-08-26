# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 413
- HTTP: 113 alive / 65 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38417
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
