# SyndProxy private pool

## Current pool

- Alive now: 716
- Gold now: 346
- HTTP: 185 alive / 73 gold
- HTTPS: 145 alive / 17 gold
- SOCKS4: 214 alive / 141 gold
- SOCKS5: 172 alive / 115 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25358
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
