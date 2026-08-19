# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 366
- HTTP: 232 alive / 88 gold
- HTTPS: 175 alive / 16 gold
- SOCKS4: 210 alive / 139 gold
- SOCKS5: 206 alive / 123 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18287
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
