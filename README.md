# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 409
- HTTP: 98 alive / 65 gold
- HTTPS: 72 alive / 15 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39235
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
