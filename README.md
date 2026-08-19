# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 342
- HTTP: 281 alive / 69 gold
- HTTPS: 206 alive / 16 gold
- SOCKS4: 189 alive / 111 gold
- SOCKS5: 236 alive / 146 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16129
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
