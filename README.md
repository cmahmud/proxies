# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 368
- HTTP: 80 alive / 43 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 183 alive / 158 gold

## Historical pool

- Discovered: 173068
- Ever alive: 33011
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
