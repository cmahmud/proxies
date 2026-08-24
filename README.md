# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 415
- HTTP: 110 alive / 72 gold
- HTTPS: 77 alive / 18 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 197 alive / 167 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33736
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
