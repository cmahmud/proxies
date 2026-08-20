# SyndProxy private pool

## Current pool

- Alive now: 1610
- Gold now: 612
- HTTP: 624 alive / 216 gold
- HTTPS: 516 alive / 116 gold
- SOCKS4: 224 alive / 135 gold
- SOCKS5: 246 alive / 145 gold

## Historical pool

- Discovered: 141135
- Ever alive: 23839
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
