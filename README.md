# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 401
- HTTP: 103 alive / 68 gold
- HTTPS: 84 alive / 16 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 173 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37331
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
