# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 431
- HTTP: 96 alive / 75 gold
- HTTPS: 51 alive / 26 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49141
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
