# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 349
- HTTP: 131 alive / 40 gold
- HTTPS: 65 alive / 9 gold
- SOCKS4: 197 alive / 155 gold
- SOCKS5: 221 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32876
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
