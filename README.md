# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 363
- HTTP: 79 alive / 46 gold
- HTTPS: 38 alive / 8 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 173622
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
