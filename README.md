# SyndProxy validated proxy pool

## Current pool

- Alive now: 684
- Gold now: 467
- HTTP: 147 alive / 96 gold
- HTTPS: 131 alive / 32 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 227 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46287
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
