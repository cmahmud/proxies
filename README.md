# SyndProxy private pool

## Current pool

- Alive now: 878
- Gold now: 395
- HTTP: 281 alive / 90 gold
- HTTPS: 180 alive / 26 gold
- SOCKS4: 209 alive / 147 gold
- SOCKS5: 208 alive / 132 gold

## Historical pool

- Discovered: 165830
- Ever alive: 32349
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
