# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 409
- HTTP: 117 alive / 64 gold
- HTTPS: 99 alive / 16 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39305
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
