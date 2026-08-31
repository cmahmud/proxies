# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 435
- HTTP: 136 alive / 71 gold
- HTTPS: 100 alive / 30 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 210 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45395
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
