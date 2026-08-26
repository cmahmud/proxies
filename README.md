# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 401
- HTTP: 87 alive / 61 gold
- HTTPS: 38 alive / 14 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38978
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
