# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 471
- HTTP: 125 alive / 96 gold
- HTTPS: 61 alive / 37 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 188 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49377
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
