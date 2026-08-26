# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 406
- HTTP: 105 alive / 62 gold
- HTTPS: 79 alive / 16 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39116
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
