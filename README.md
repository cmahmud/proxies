# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 410
- HTTP: 122 alive / 60 gold
- HTTPS: 141 alive / 18 gold
- SOCKS4: 180 alive / 165 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41270
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
