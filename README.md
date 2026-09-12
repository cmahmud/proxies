# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 466
- HTTP: 130 alive / 94 gold
- HTTPS: 47 alive / 34 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49413
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
