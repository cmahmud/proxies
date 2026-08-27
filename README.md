# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 413
- HTTP: 112 alive / 64 gold
- HTTPS: 135 alive / 19 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41356
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
