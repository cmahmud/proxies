# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 454
- HTTP: 136 alive / 87 gold
- HTTPS: 89 alive / 34 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46984
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
