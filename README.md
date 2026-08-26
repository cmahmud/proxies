# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 401
- HTTP: 89 alive / 60 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38978
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
