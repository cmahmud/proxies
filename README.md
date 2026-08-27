# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 415
- HTTP: 101 alive / 72 gold
- HTTPS: 117 alive / 20 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41923
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
