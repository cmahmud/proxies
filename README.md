# SyndProxy validated proxy pool

## Current pool

- Alive now: 446
- Gold now: 362
- HTTP: 72 alive / 44 gold
- HTTPS: 37 alive / 8 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 173 alive / 155 gold

## Historical pool

- Discovered: 173071
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
