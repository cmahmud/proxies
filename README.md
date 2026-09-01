# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 454
- HTTP: 138 alive / 88 gold
- HTTPS: 100 alive / 34 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 200 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46986
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
