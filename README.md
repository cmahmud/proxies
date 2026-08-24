# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 384
- HTTP: 93 alive / 54 gold
- HTTPS: 37 alive / 10 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33459
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
