# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 406
- HTTP: 96 alive / 62 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38472
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
