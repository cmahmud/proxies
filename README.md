# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 393
- HTTP: 272 alive / 89 gold
- HTTPS: 171 alive / 25 gold
- SOCKS4: 217 alive / 147 gold
- SOCKS5: 220 alive / 132 gold

## Historical pool

- Discovered: 165830
- Ever alive: 32349
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
