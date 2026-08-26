# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 414
- HTTP: 103 alive / 66 gold
- HTTPS: 85 alive / 22 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 174 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37767
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
