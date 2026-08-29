# SyndProxy validated proxy pool

## Current pool

- Alive now: 409
- Gold now: 305
- HTTP: 53 alive / 35 gold
- HTTPS: 24 alive / 5 gold
- SOCKS4: 163 alive / 142 gold
- SOCKS5: 169 alive / 123 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43543
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
