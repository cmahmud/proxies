# SyndProxy private pool

## Current pool

- Alive now: 1728
- Gold now: 657
- HTTP: 719 alive / 240 gold
- HTTPS: 573 alive / 140 gold
- SOCKS4: 206 alive / 135 gold
- SOCKS5: 230 alive / 142 gold

## Historical pool

- Discovered: 142719
- Ever alive: 24520
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
