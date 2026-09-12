# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 471
- HTTP: 135 alive / 99 gold
- HTTPS: 57 alive / 35 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49356
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
