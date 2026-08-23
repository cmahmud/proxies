# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 342
- HTTP: 137 alive / 39 gold
- HTTPS: 74 alive / 9 gold
- SOCKS4: 175 alive / 153 gold
- SOCKS5: 198 alive / 141 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32879
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
