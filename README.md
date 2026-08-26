# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 406
- HTTP: 108 alive / 64 gold
- HTTPS: 69 alive / 18 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38630
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
