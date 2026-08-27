# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 406
- HTTP: 112 alive / 65 gold
- HTTPS: 176 alive / 16 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41085
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
