# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 396
- HTTP: 107 alive / 57 gold
- HTTPS: 39 alive / 15 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38975
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
