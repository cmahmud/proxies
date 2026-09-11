# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 429
- HTTP: 97 alive / 71 gold
- HTTPS: 48 alive / 29 gold
- SOCKS4: 179 alive / 168 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49049
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
