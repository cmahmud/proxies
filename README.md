# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 372
- HTTP: 195 alive / 69 gold
- HTTPS: 147 alive / 20 gold
- SOCKS4: 215 alive / 147 gold
- SOCKS5: 212 alive / 136 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26150
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
