# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 447
- HTTP: 102 alive / 84 gold
- HTTPS: 53 alive / 30 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49193
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
