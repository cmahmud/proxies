# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 419
- HTTP: 90 alive / 67 gold
- HTTPS: 55 alive / 24 gold
- SOCKS4: 187 alive / 166 gold
- SOCKS5: 176 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49036
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
