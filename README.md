# SyndProxy private pool

## Current pool

- Alive now: 874
- Gold now: 392
- HTTP: 269 alive / 88 gold
- HTTPS: 183 alive / 25 gold
- SOCKS4: 211 alive / 147 gold
- SOCKS5: 211 alive / 132 gold

## Historical pool

- Discovered: 165830
- Ever alive: 32349
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
