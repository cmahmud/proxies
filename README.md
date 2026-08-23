# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 358
- HTTP: 78 alive / 39 gold
- HTTPS: 37 alive / 9 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 185 alive / 156 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
