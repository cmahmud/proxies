# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 406
- HTTP: 115 alive / 79 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 170 alive / 150 gold
- SOCKS5: 184 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48068
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
