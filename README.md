# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 465
- HTTP: 442 alive / 125 gold
- HTTPS: 268 alive / 71 gold
- SOCKS4: 206 alive / 128 gold
- SOCKS5: 254 alive / 141 gold

## Historical pool

- Discovered: 117107
- Ever alive: 17214
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
