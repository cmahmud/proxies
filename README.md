# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 408
- HTTP: 109 alive / 66 gold
- HTTPS: 69 alive / 16 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38373
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
