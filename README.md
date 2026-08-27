# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 413
- HTTP: 115 alive / 70 gold
- HTTPS: 172 alive / 16 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41210
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
