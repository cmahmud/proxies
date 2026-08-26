# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 411
- HTTP: 126 alive / 73 gold
- HTTPS: 174 alive / 18 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40414
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
