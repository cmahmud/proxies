# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 433
- HTTP: 101 alive / 76 gold
- HTTPS: 50 alive / 28 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49145
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
