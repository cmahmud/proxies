# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 416
- HTTP: 101 alive / 71 gold
- HTTPS: 141 alive / 19 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41294
- Ever gold: 1321

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
