# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 480
- HTTP: 157 alive / 102 gold
- HTTPS: 125 alive / 40 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45247
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
