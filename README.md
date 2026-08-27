# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 401
- HTTP: 98 alive / 61 gold
- HTTPS: 171 alive / 17 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41052
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
