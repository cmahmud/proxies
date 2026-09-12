# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 448
- HTTP: 118 alive / 90 gold
- HTTPS: 54 alive / 30 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49301
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
