# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 500
- HTTP: 376 alive / 165 gold
- HTTPS: 238 alive / 93 gold
- SOCKS4: 194 alive / 110 gold
- SOCKS5: 230 alive / 132 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18775
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
