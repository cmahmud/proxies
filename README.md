# SyndProxy validated proxy pool

## Current pool

- Alive now: 729
- Gold now: 465
- HTTP: 161 alive / 96 gold
- HTTPS: 148 alive / 31 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 236 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46275
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
