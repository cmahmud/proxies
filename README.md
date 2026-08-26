# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 412
- HTTP: 102 alive / 63 gold
- HTTPS: 73 alive / 14 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 210 alive / 173 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38173
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
