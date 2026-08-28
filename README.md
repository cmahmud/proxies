# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 403
- HTTP: 86 alive / 61 gold
- HTTPS: 48 alive / 15 gold
- SOCKS4: 178 alive / 165 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42836
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
