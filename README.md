# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 496
- HTTP: 423 alive / 164 gold
- HTTPS: 232 alive / 90 gold
- SOCKS4: 193 alive / 110 gold
- SOCKS5: 229 alive / 132 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18764
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
