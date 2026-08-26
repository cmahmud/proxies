# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 373
- HTTP: 109 alive / 65 gold
- HTTPS: 64 alive / 16 gold
- SOCKS4: 150 alive / 140 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38778
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
