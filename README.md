# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 448
- HTTP: 120 alive / 87 gold
- HTTPS: 50 alive / 29 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49263
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
