# SyndProxy private pool

## Current pool

- Alive now: 719
- Gold now: 366
- HTTP: 205 alive / 75 gold
- HTTPS: 111 alive / 19 gold
- SOCKS4: 182 alive / 127 gold
- SOCKS5: 221 alive / 145 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25607
- Ever gold: 1068

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
