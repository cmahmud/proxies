# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 406
- HTTP: 91 alive / 65 gold
- HTTPS: 37 alive / 21 gold
- SOCKS4: 167 alive / 148 gold
- SOCKS5: 183 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48812
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
