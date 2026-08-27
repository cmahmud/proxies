# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 415
- HTTP: 91 alive / 61 gold
- HTTPS: 100 alive / 21 gold
- SOCKS4: 182 alive / 167 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41532
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
