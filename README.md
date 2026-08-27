# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 415
- HTTP: 119 alive / 69 gold
- HTTPS: 127 alive / 17 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41385
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
