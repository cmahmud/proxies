# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 389
- HTTP: 133 alive / 70 gold
- HTTPS: 173 alive / 20 gold
- SOCKS4: 160 alive / 147 gold
- SOCKS5: 180 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39752
- Ever gold: 1303

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
