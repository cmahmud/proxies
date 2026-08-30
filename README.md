# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 446
- HTTP: 109 alive / 81 gold
- HTTPS: 45 alive / 30 gold
- SOCKS4: 166 alive / 163 gold
- SOCKS5: 180 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43684
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
