# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 415
- HTTP: 119 alive / 85 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 163 alive / 147 gold
- SOCKS5: 191 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48048
- Ever gold: 1515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
