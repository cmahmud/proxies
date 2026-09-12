# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 355
- HTTP: 85 alive / 60 gold
- HTTPS: 36 alive / 16 gold
- SOCKS4: 147 alive / 133 gold
- SOCKS5: 161 alive / 146 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49558
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
