# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 425
- HTTP: 117 alive / 74 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34923
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
