# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 406
- HTTP: 91 alive / 67 gold
- HTTPS: 80 alive / 19 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37694
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
