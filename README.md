# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 388
- HTTP: 310 alive / 90 gold
- HTTPS: 181 alive / 15 gold
- SOCKS4: 232 alive / 155 gold
- SOCKS5: 203 alive / 128 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18236
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
