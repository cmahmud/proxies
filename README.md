# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 399
- HTTP: 94 alive / 63 gold
- HTTPS: 31 alive / 19 gold
- SOCKS4: 160 alive / 146 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48805
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
