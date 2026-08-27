# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 403
- HTTP: 101 alive / 62 gold
- HTTPS: 129 alive / 15 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41381
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
