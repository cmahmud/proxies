# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 404
- HTTP: 100 alive / 60 gold
- HTTPS: 74 alive / 16 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39122
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
