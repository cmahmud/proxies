# SyndProxy validated proxy pool

## Current pool

- Alive now: 438
- Gold now: 366
- HTTP: 68 alive / 45 gold
- HTTPS: 33 alive / 8 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 175 alive / 157 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33018
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
