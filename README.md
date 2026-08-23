# SyndProxy validated proxy pool

## Current pool

- Alive now: 685
- Gold now: 348
- HTTP: 218 alive / 39 gold
- HTTPS: 46 alive / 10 gold
- SOCKS4: 184 alive / 154 gold
- SOCKS5: 237 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32872
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
