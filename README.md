# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 371
- HTTP: 65 alive / 46 gold
- HTTPS: 47 alive / 8 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 170 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43525
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
