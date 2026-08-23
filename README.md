# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 379
- HTTP: 92 alive / 62 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 174154
- Ever alive: 33069
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
