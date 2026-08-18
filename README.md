# SyndProxy private pool

## Current pool

- Alive now: 637
- Gold now: 189
- HTTP: 174 alive / 34 gold
- HTTPS: 108 alive / 10 gold
- SOCKS4: 196 alive / 77 gold
- SOCKS5: 159 alive / 68 gold

## Historical pool

- Discovered: 82934
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
