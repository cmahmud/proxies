# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 498
- HTTP: 413 alive / 164 gold
- HTTPS: 235 alive / 92 gold
- SOCKS4: 195 alive / 110 gold
- SOCKS5: 237 alive / 132 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18769
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
