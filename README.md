# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 406
- HTTP: 91 alive / 60 gold
- HTTPS: 77 alive / 17 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39086
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
