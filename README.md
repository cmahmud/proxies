# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 415
- HTTP: 110 alive / 66 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 198 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45519
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
