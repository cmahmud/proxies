# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 342
- HTTP: 54 alive / 44 gold
- HTTPS: 41 alive / 7 gold
- SOCKS4: 164 alive / 144 gold
- SOCKS5: 170 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43543
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
