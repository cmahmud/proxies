# SyndProxy private pool

## Current pool

- Alive now: 736
- Gold now: 361
- HTTP: 201 alive / 82 gold
- HTTPS: 134 alive / 19 gold
- SOCKS4: 207 alive / 134 gold
- SOCKS5: 194 alive / 126 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26600
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
