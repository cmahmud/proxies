# SyndProxy private pool

## Current pool

- Alive now: 672
- Gold now: 383
- HTTP: 181 alive / 64 gold
- HTTPS: 85 alive / 20 gold
- SOCKS4: 196 alive / 148 gold
- SOCKS5: 210 alive / 151 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25731
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
