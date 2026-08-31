# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 472
- HTTP: 152 alive / 97 gold
- HTTPS: 121 alive / 37 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 196 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45187
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
