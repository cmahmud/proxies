# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 457
- HTTP: 123 alive / 88 gold
- HTTPS: 120 alive / 33 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46714
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
