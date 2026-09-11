# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 447
- HTTP: 114 alive / 85 gold
- HTTPS: 51 alive / 28 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49235
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
