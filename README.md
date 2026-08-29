# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 353
- HTTP: 56 alive / 35 gold
- HTTPS: 24 alive / 5 gold
- SOCKS4: 160 alive / 155 gold
- SOCKS5: 175 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43582
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
