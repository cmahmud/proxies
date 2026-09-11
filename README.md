# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 436
- HTTP: 101 alive / 77 gold
- HTTPS: 46 alive / 27 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49170
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
