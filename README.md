# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 422
- HTTP: 127 alive / 65 gold
- HTTPS: 71 alive / 25 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 207 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45527
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
