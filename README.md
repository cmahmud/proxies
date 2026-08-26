# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 401
- HTTP: 96 alive / 59 gold
- HTTPS: 61 alive / 16 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39202
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
