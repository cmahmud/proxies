# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 383
- HTTP: 104 alive / 55 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33459
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
