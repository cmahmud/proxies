# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 365
- HTTP: 82 alive / 45 gold
- HTTPS: 40 alive / 9 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 176 alive / 156 gold

## Historical pool

- Discovered: 173622
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
