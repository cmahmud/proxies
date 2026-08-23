# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 361
- HTTP: 100 alive / 40 gold
- HTTPS: 44 alive / 8 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 188 alive / 158 gold

## Historical pool

- Discovered: 173622
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
