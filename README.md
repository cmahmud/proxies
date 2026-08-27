# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 414
- HTTP: 114 alive / 65 gold
- HTTPS: 159 alive / 18 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41258
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
