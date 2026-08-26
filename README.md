# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 411
- HTTP: 102 alive / 65 gold
- HTTPS: 89 alive / 13 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 207 alive / 171 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38166
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
