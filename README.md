# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 404
- HTTP: 86 alive / 60 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38546
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
