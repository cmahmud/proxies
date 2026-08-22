# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 384
- HTTP: 239 alive / 79 gold
- HTTPS: 167 alive / 21 gold
- SOCKS4: 212 alive / 147 gold
- SOCKS5: 204 alive / 137 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31875
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
