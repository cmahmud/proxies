# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 415
- HTTP: 107 alive / 71 gold
- HTTPS: 173 alive / 16 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41211
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
