# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 291
- HTTP: 310 alive / 27 gold
- HTTPS: 200 alive / 4 gold
- SOCKS4: 250 alive / 144 gold
- SOCKS5: 248 alive / 116 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12744
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
