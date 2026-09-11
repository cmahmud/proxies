# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 447
- HTTP: 113 alive / 85 gold
- HTTPS: 49 alive / 27 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49238
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
