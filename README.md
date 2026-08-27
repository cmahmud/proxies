# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 409
- HTTP: 103 alive / 64 gold
- HTTPS: 170 alive / 17 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41070
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
