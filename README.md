# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 411
- HTTP: 179 alive / 84 gold
- HTTPS: 154 alive / 25 gold
- SOCKS4: 210 alive / 156 gold
- SOCKS5: 225 alive / 146 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26969
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
