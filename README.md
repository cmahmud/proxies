# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 413
- HTTP: 113 alive / 68 gold
- HTTPS: 159 alive / 16 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41155
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
