# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 422
- HTTP: 92 alive / 69 gold
- HTTPS: 58 alive / 23 gold
- SOCKS4: 188 alive / 167 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49065
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
