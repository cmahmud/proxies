# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 454
- HTTP: 125 alive / 85 gold
- HTTPS: 128 alive / 33 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46841
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
