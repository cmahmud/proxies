# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 401
- HTTP: 107 alive / 59 gold
- HTTPS: 75 alive / 14 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 202 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38290
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
