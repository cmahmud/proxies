# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 358
- HTTP: 87 alive / 38 gold
- HTTPS: 36 alive / 8 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 184 alive / 156 gold

## Historical pool

- Discovered: 173622
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
