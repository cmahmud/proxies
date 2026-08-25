# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 398
- HTTP: 97 alive / 66 gold
- HTTPS: 70 alive / 17 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 165 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37272
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
