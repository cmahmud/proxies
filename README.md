# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 460
- HTTP: 122 alive / 90 gold
- HTTPS: 128 alive / 36 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46711
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
