# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 469
- HTTP: 123 alive / 92 gold
- HTTPS: 135 alive / 37 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 230 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45911
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
