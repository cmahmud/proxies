# SyndProxy validated proxy pool

## Current pool

- Alive now: 705
- Gold now: 470
- HTTP: 161 alive / 99 gold
- HTTPS: 128 alive / 32 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 234 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46284
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
