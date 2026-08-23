# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 348
- HTTP: 205 alive / 39 gold
- HTTPS: 43 alive / 9 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 192 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32867
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
