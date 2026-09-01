# SyndProxy validated proxy pool

## Current pool

- Alive now: 728
- Gold now: 463
- HTTP: 160 alive / 95 gold
- HTTPS: 146 alive / 31 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 238 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46275
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
