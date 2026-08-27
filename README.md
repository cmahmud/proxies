# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 418
- HTTP: 103 alive / 68 gold
- HTTPS: 144 alive / 19 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41228
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
