# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 401
- HTTP: 105 alive / 58 gold
- HTTPS: 74 alive / 16 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39023
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
