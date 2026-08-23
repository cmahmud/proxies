# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 361
- HTTP: 90 alive / 41 gold
- HTTPS: 39 alive / 9 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 178 alive / 155 gold

## Historical pool

- Discovered: 173622
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
