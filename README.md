# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 468
- HTTP: 128 alive / 94 gold
- HTTPS: 116 alive / 38 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46368
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
