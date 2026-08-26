# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 409
- HTTP: 95 alive / 64 gold
- HTTPS: 100 alive / 18 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38045
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
