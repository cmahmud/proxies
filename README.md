# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 415
- HTTP: 85 alive / 68 gold
- HTTPS: 115 alive / 22 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42589
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
