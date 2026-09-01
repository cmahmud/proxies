# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 475
- HTTP: 150 alive / 97 gold
- HTTPS: 125 alive / 40 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46954
- Ever gold: 1461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
