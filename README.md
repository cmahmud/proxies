# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 426
- HTTP: 138 alive / 65 gold
- HTTPS: 71 alive / 23 gold
- SOCKS4: 201 alive / 161 gold
- SOCKS5: 223 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35867
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
