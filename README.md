# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 363
- HTTP: 77 alive / 42 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 175 alive / 156 gold

## Historical pool

- Discovered: 173071
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
