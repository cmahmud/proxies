# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 370
- HTTP: 73 alive / 50 gold
- HTTPS: 61 alive / 12 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 171 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43491
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
