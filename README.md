# SyndProxy private pool

## Current pool

- Alive now: 1376
- Gold now: 585
- HTTP: 480 alive / 195 gold
- HTTPS: 367 alive / 101 gold
- SOCKS4: 251 alive / 141 gold
- SOCKS5: 278 alive / 148 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23298
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
