# SyndProxy private pool

## Current pool

- Alive now: 1255
- Gold now: 571
- HTTP: 419 alive / 186 gold
- HTTPS: 349 alive / 97 gold
- SOCKS4: 237 alive / 135 gold
- SOCKS5: 250 alive / 153 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23285
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
