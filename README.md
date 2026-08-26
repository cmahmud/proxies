# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 401
- HTTP: 104 alive / 65 gold
- HTTPS: 80 alive / 16 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38704
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
