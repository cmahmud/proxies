# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 412
- HTTP: 94 alive / 67 gold
- HTTPS: 72 alive / 20 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38609
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
