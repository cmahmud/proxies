# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 415
- HTTP: 110 alive / 70 gold
- HTTPS: 123 alive / 17 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41401
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
