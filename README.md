# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 400
- HTTP: 97 alive / 58 gold
- HTTPS: 76 alive / 16 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38450
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
