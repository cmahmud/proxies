# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 472
- HTTP: 138 alive / 95 gold
- HTTPS: 121 alive / 40 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46934
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
