# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 400
- HTTP: 89 alive / 68 gold
- HTTPS: 92 alive / 15 gold
- SOCKS4: 158 alive / 154 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43256
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
