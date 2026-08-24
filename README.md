# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 389
- HTTP: 99 alive / 49 gold
- HTTPS: 43 alive / 13 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33548
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
