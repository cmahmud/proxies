# SyndProxy validated proxy pool

## Current pool

- Alive now: 733
- Gold now: 463
- HTTP: 160 alive / 95 gold
- HTTPS: 145 alive / 30 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 242 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46275
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
