# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 413
- HTTP: 127 alive / 76 gold
- HTTPS: 153 alive / 21 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40243
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
