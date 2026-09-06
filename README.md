# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 384
- HTTP: 102 alive / 71 gold
- HTTPS: 30 alive / 11 gold
- SOCKS4: 172 alive / 149 gold
- SOCKS5: 179 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48228
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
