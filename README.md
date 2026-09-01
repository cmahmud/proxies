# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 467
- HTTP: 142 alive / 96 gold
- HTTPS: 115 alive / 33 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46321
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
