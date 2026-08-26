# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 404
- HTTP: 106 alive / 60 gold
- HTTPS: 76 alive / 16 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39118
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
