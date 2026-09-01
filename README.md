# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 425
- HTTP: 85 alive / 66 gold
- HTTPS: 76 alive / 27 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47154
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
