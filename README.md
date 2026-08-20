# SyndProxy private pool

## Current pool

- Alive now: 1309
- Gold now: 574
- HTTP: 442 alive / 188 gold
- HTTPS: 350 alive / 98 gold
- SOCKS4: 255 alive / 137 gold
- SOCKS5: 262 alive / 151 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23288
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
