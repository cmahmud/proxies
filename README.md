# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 256
- HTTP: 441 alive / 31 gold
- HTTPS: 168 alive / 5 gold
- SOCKS4: 229 alive / 116 gold
- SOCKS5: 230 alive / 104 gold

## Historical pool

- Discovered: 95404
- Ever alive: 10984
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
