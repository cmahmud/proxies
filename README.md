# SyndProxy private pool

## Current pool

- Alive now: 651
- Gold now: 250
- HTTP: 155 alive / 34 gold
- HTTPS: 91 alive / 7 gold
- SOCKS4: 210 alive / 125 gold
- SOCKS5: 195 alive / 84 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9352
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
