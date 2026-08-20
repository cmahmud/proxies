# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 390
- HTTP: 321 alive / 84 gold
- HTTPS: 216 alive / 21 gold
- SOCKS4: 199 alive / 130 gold
- SOCKS5: 233 alive / 155 gold

## Historical pool

- Discovered: 144740
- Ever alive: 24992
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
