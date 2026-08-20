# SyndProxy private pool

## Current pool

- Alive now: 1923
- Gold now: 700
- HTTP: 747 alive / 231 gold
- HTTPS: 612 alive / 146 gold
- SOCKS4: 230 alive / 155 gold
- SOCKS5: 334 alive / 168 gold

## Historical pool

- Discovered: 142714
- Ever alive: 24453
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
