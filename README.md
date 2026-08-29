# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 380
- HTTP: 83 alive / 59 gold
- HTTPS: 92 alive / 17 gold
- SOCKS4: 161 alive / 150 gold
- SOCKS5: 167 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43337
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
