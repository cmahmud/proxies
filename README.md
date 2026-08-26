# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 399
- HTTP: 97 alive / 54 gold
- HTTPS: 76 alive / 16 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39139
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
