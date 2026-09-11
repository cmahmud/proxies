# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 430
- HTTP: 94 alive / 75 gold
- HTTPS: 55 alive / 26 gold
- SOCKS4: 186 alive / 168 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49090
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
