# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 391
- HTTP: 165 alive / 66 gold
- HTTPS: 123 alive / 22 gold
- SOCKS4: 171 alive / 150 gold
- SOCKS5: 195 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39550
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
