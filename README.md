# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 362
- HTTP: 77 alive / 45 gold
- HTTPS: 38 alive / 8 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 177 alive / 154 gold

## Historical pool

- Discovered: 173071
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
