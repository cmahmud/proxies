# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 450
- HTTP: 120 alive / 89 gold
- HTTPS: 51 alive / 31 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49290
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
