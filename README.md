# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 401
- HTTP: 106 alive / 61 gold
- HTTPS: 74 alive / 10 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 201 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38221
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
