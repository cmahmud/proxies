# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 470
- HTTP: 136 alive / 95 gold
- HTTPS: 103 alive / 36 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 212 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46423
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
