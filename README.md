# SyndProxy validated proxy pool

## Current pool

- Alive now: 723
- Gold now: 467
- HTTP: 160 alive / 97 gold
- HTTPS: 142 alive / 32 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 237 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46276
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
