# SyndProxy validated proxy pool

## Current pool

- Alive now: 454
- Gold now: 364
- HTTP: 73 alive / 44 gold
- HTTPS: 36 alive / 9 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33017
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
