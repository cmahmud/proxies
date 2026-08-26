# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 393
- HTTP: 173 alive / 69 gold
- HTTPS: 85 alive / 22 gold
- SOCKS4: 170 alive / 148 gold
- SOCKS5: 219 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39400
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
