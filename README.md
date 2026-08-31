# SyndProxy validated proxy pool

## Current pool

- Alive now: 668
- Gold now: 463
- HTTP: 136 alive / 93 gold
- HTTPS: 142 alive / 29 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 218 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45994
- Ever gold: 1438

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
