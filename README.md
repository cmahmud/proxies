# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 400
- HTTP: 88 alive / 65 gold
- HTTPS: 38 alive / 17 gold
- SOCKS4: 186 alive / 155 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48146
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
