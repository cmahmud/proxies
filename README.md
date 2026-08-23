# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 364
- HTTP: 86 alive / 43 gold
- HTTPS: 40 alive / 9 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 178 alive / 156 gold

## Historical pool

- Discovered: 173622
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
