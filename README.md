# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 365
- HTTP: 77 alive / 43 gold
- HTTPS: 37 alive / 10 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 181 alive / 156 gold

## Historical pool

- Discovered: 173068
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
