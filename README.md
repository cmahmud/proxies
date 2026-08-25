# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 393
- HTTP: 94 alive / 62 gold
- HTTPS: 80 alive / 17 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 173 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37348
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
