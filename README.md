# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 404
- HTTP: 90 alive / 61 gold
- HTTPS: 60 alive / 16 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38984
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
