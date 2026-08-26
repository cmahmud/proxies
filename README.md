# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 413
- HTTP: 141 alive / 75 gold
- HTTPS: 153 alive / 21 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40252
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
