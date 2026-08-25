# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 422
- HTTP: 91 alive / 70 gold
- HTTPS: 50 alive / 22 gold
- SOCKS4: 214 alive / 162 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37125
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
