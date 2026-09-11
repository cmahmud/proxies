# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 449
- HTTP: 126 alive / 89 gold
- HTTPS: 52 alive / 30 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49254
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
