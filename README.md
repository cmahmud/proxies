# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 444
- HTTP: 116 alive / 85 gold
- HTTPS: 55 alive / 28 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49272
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
