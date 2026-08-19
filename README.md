# SyndProxy private pool

## Current pool

- Alive now: 1172
- Gold now: 571
- HTTP: 444 alive / 186 gold
- HTTPS: 315 alive / 111 gold
- SOCKS4: 210 alive / 130 gold
- SOCKS5: 203 alive / 144 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19827
- Ever gold: 801

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
