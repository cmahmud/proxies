# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 410
- HTTP: 97 alive / 65 gold
- HTTPS: 69 alive / 16 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39236
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
