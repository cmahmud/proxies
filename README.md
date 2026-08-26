# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 404
- HTTP: 104 alive / 61 gold
- HTTPS: 89 alive / 16 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39029
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
