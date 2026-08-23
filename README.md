# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 364
- HTTP: 80 alive / 46 gold
- HTTPS: 39 alive / 8 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 176 alive / 155 gold

## Historical pool

- Discovered: 173622
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
