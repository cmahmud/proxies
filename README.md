# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 411
- HTTP: 120 alive / 83 gold
- HTTPS: 69 alive / 24 gold
- SOCKS4: 167 alive / 145 gold
- SOCKS5: 184 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48051
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
