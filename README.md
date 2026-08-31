# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 463
- HTTP: 128 alive / 90 gold
- HTTPS: 134 alive / 32 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 217 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45960
- Ever gold: 1438

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
