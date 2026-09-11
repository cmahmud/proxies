# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 447
- HTTP: 113 alive / 84 gold
- HTTPS: 51 alive / 30 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49181
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
