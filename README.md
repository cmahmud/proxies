# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 574
- HTTP: 302 alive / 190 gold
- HTTPS: 222 alive / 98 gold
- SOCKS4: 216 alive / 137 gold
- SOCKS5: 250 alive / 149 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23240
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
