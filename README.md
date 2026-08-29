# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 358
- HTTP: 87 alive / 63 gold
- HTTPS: 82 alive / 16 gold
- SOCKS4: 158 alive / 142 gold
- SOCKS5: 174 alive / 137 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43323
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
