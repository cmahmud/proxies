# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 401
- HTTP: 103 alive / 68 gold
- HTTPS: 76 alive / 15 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37326
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
