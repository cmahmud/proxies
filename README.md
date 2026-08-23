# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 392
- HTTP: 120 alive / 68 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 196 alive / 158 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33178
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
