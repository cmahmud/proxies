# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 415
- HTTP: 150 alive / 73 gold
- HTTPS: 65 alive / 19 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 198 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33740
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
