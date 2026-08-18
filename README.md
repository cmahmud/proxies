# SyndProxy private pool

## Current pool

- Alive now: 854
- Gold now: 261
- HTTP: 278 alive / 30 gold
- HTTPS: 137 alive / 3 gold
- SOCKS4: 214 alive / 119 gold
- SOCKS5: 225 alive / 109 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12023
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
