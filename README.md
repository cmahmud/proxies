# SyndProxy private pool

## Current pool

- Alive now: 1833
- Gold now: 640
- HTTP: 703 alive / 222 gold
- HTTPS: 609 alive / 116 gold
- SOCKS4: 220 alive / 145 gold
- SOCKS5: 301 alive / 157 gold

## Historical pool

- Discovered: 142692
- Ever alive: 24281
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
