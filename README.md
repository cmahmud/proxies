# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 400
- HTTP: 91 alive / 67 gold
- HTTPS: 86 alive / 16 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43260
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
