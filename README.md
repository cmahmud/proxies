# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 404
- HTTP: 96 alive / 72 gold
- HTTPS: 72 alive / 18 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 167 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37214
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
