# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 347
- HTTP: 190 alive / 40 gold
- HTTPS: 49 alive / 9 gold
- SOCKS4: 176 alive / 154 gold
- SOCKS5: 234 alive / 144 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32873
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
