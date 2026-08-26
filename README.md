# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 401
- HTTP: 102 alive / 59 gold
- HTTPS: 64 alive / 13 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38282
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
