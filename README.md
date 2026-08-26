# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 406
- HTTP: 97 alive / 62 gold
- HTTPS: 95 alive / 16 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38316
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
