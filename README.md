# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 389
- HTTP: 289 alive / 86 gold
- HTTPS: 170 alive / 24 gold
- SOCKS4: 210 alive / 147 gold
- SOCKS5: 212 alive / 132 gold

## Historical pool

- Discovered: 165830
- Ever alive: 32349
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
