# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 407
- HTTP: 92 alive / 62 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42836
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
