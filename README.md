# SyndProxy validated proxy pool

## Current pool

- Alive now: 452
- Gold now: 362
- HTTP: 79 alive / 41 gold
- HTTPS: 33 alive / 10 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 175 alive / 156 gold

## Historical pool

- Discovered: 173071
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
