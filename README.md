# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 339
- HTTP: 118 alive / 39 gold
- HTTPS: 49 alive / 9 gold
- SOCKS4: 165 alive / 149 gold
- SOCKS5: 195 alive / 142 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32883
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
