# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 415
- HTTP: 91 alive / 61 gold
- HTTPS: 73 alive / 21 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36238
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
