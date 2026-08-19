# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 459
- HTTP: 394 alive / 128 gold
- HTTPS: 280 alive / 74 gold
- SOCKS4: 225 alive / 115 gold
- SOCKS5: 252 alive / 142 gold

## Historical pool

- Discovered: 117109
- Ever alive: 17262
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
