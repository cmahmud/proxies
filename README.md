# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 402
- HTTP: 89 alive / 60 gold
- HTTPS: 72 alive / 17 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38459
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
