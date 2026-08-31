# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 484
- HTTP: 165 alive / 103 gold
- HTTPS: 138 alive / 43 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 199 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45238
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
